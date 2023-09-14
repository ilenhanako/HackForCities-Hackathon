#Parameterized quantum circuit using QAOA, employing RXX, RZZ, and single-qubit rotation gates:
import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, assemble, IBMQ
from qiskit.providers.ibmq.job import job_monitor
from qiskit.visualization import plot_histogram

# Save and load your IBM Q account
IBMQ.save_account('36b1770273555e2252601dc0895db9670844228979de0798ce59cc99f4388c56602c7105510e3ec3ec10e471b05afec600779b983540dbe084f4d1c41708832d')  # Uncomment and replace 'YOUR_API_TOKEN' if not saved yet
IBMQ.load_account()

# Define the QAOA circuit
def qaoa_circuit(graph, p, beta, gamma):
    """
    Create a QAOA circuit given the graph, depth p, and angles beta and gamma.
    """
    n = len(graph)
    qc = QuantumCircuit(n)
    
    # Initial state preparation (Hadamard on every qubit)
    for qubit in range(n):
        qc.h(qubit)

    # QAOA alternating operator sequence
    for layer in range(p):
        # Problem unitary
        for qubit, connections in enumerate(graph):
            for conn in connections:
                qc.rzz(2*gamma[layer], qubit, conn)  # RZZ gate
                qc.rxx(2*gamma[layer], qubit, conn)  # RXX gate

        # Mixer unitary
        for qubit in range(n):
            qc.rx(2*beta[layer], qubit)
            qc.ry(2*beta[layer], qubit)
            qc.rz(2*beta[layer], qubit)
    
    return qc

# Example usage:
# Define a simple graph: a triangle
graph = [
    [1, 2],
    [0, 2],
    [0, 1]
]

p = 4  # Depth of the circuit
beta = np.random.uniform(0, np.pi, p)
gamma = np.random.uniform(0, np.pi, p)

qc = qaoa_circuit(graph, p, beta, gamma)
qc.measure_all()

# Visualize the circuit
qc.draw(output="mpl")

# Transpile and run on a quantum processor
provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_qasm_simulator')  # Using the simulator for demonstration

t_qc = transpile(qc, backend=backend)
qobj = assemble(t_qc)
job = backend.run(qobj)

# Monitor the job
job_monitor(job)

# Get the results
results = job.result()
counts = results.get_counts()
print(counts)
plot_histogram(counts).show()

'''
#GROVER ALGORITHM
# Built-in modules
import math

# Imports from Qiskit
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator, MCMT, ZGate
from qiskit.visualization import plot_distribution

# Imports from Qiskit Runtime
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

service = QiskitRuntimeService()
sim = service.get_backend("ibmq_qasm_simulator")
backend = service.get_backend("ibm_brisbane")
'''