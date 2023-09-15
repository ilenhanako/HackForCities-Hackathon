#initialization
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

# importing Qiskit
from qiskit import IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

# import basic plot tools
from qiskit.tools.visualization import plot_histogram

# phase oracle using controlled-Z gate, visualizes oracle using Qiskit's circuit drawer
def phase_oracle(circuit, register):
    circuit.cz(register[0], register[1])
    # function applies the controlled-Z (CZ) gate on the quantum register.
    # The CZ gate flips the sign (phase) of the state of the target qubit if the control qubit is in the state |1⟩.
qr = QuantumRegister(4)
# creates a new quantum register named 'qr' with 2 qubits
oracleCircuit = QuantumCircuit(qr)
phase_oracle(oracleCircuit, qr)
# draws the quantum circuit oracleCircuit using a Matplotlib-based visual representation
oracleCircuit.draw(output="mpl")

# Amplitude Amplification Module or Diffusion Circuit
# Set up circuit for inversion about the average
def inversion_about_average(circuit, register):
    """Apply inversion about the average step of Grover's algorithm."""
    circuit.h(register)
    circuit.x(register)
    circuit.h(register[1])
    circuit.cx(register[0], register[1])
    circuit.h(register[1])
    circuit.x(register)
    circuit.h(register)

qAverage = QuantumCircuit(qr)
inversion_about_average(qAverage, qr)
qAverage.draw(output='mpl')

''''
constructs a quantum circuit for Grover's algorithm by initializing a superposition of states, applying an oracle, performing amplitude amplification, and then measuring the result.
'''
# create quantum register, 'qr', with 2 qubits
# create classical register, 'cr', with 2 bits. Classical register used to store results after measurement of quantum register
qr = QuantumRegister(4)
cr = ClassicalRegister(4)

# Hadamard gate ('h') applied to both qubits in quantum register
# Hadamard gate creates superposition of both qubits, |0⟩ and |1⟩
groverCircuit = QuantumCircuit(qr,cr)
groverCircuit.h(qr)

# increases the probability amplitude of the marked state while decreasing the amplitude of the unmarked states.
# more probable to measure desired state
phase_oracle(groverCircuit, qr)
inversion_about_average(groverCircuit, qr)

groverCircuit.measure(qr,cr)
groverCircuit.draw(output="mpl")


# Load our saved IBMQ accounts and get the least busy backend device
IBMQ.save_account('36b1770273555e2252601dc0895db9670844228979de0798ce59cc99f4388c56602c7105510e3ec3ec10e471b05afec600779b983540dbe084f4d1c41708832d')
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
backend_lb = least_busy(provider.backends(filters=lambda b: b.configuration().n_qubits >= 3 and
                                   not b.configuration().simulator and b.status().operational==True))
print("Least busy backend: ", backend_lb)


# Run our circuit on the least busy backend. Monitor the execution of the job in the queue
from qiskit.tools.monitor import job_monitor
backend = backend_lb
shots = 1024
job_exp = execute(groverCircuit, backend=backend, shots=shots)
job_monitor(job_exp, interval = 2)




# COMBINATION
# ERROR MITIGATION: Qiskit's Ignis Module

#...code for grover
# Importing Ignis error mitigation tools
from qiskit.ignis.mitigation.measurement import (complete_meas_cal, CompleteMeasFitter)

# Generate calibration circuits
meas_calibs, state_labels = complete_meas_cal(qr=qr, circlabel='mcal')

# Execute the calibration circuits
cal_job = execute(meas_calibs, backend=backend, shots=shots, optimization_level=0)
print(cal_job.job_id())
job_monitor(cal_job)
cal_results = cal_job.result()

# Fit the calibration results to construct a correction matrix
meas_fitter = CompleteMeasFitter(cal_results, state_labels, circlabel='mcal')
print(meas_fitter.cal_matrix)

# Get the filter object
meas_filter = meas_fitter.filter

# Apply the filter to the results from your Grover circuit
mitigated_results = meas_filter.apply(results)
mitigated_counts = mitigated_results.get_counts(groverCircuit)

# Plot the results
from qiskit.visualization import plot_histogram
plot_histogram([answer, mitigated_counts], legend=['raw', 'mitigated'])

# get the results from the computation
results = job_exp.result()
answer = results.get_counts(groverCircuit)
plot_histogram(answer)

