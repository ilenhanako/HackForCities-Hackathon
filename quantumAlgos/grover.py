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
qr = QuantumRegister(2)
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
qr = QuantumRegister(2)
cr = ClassicalRegister(2)

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


# get the results from the computation
results = job_exp.result()
answer = results.get_counts(groverCircuit)
plot_histogram(answer)