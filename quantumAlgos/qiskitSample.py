import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit.providers.ibmq import IBMQ
from qiskit.providers.ibmq.job import job_monitor
from qiskit.visualization import plot_histogram

# Initialize quantum circuit
bell = QuantumCircuit(2, 2)

# Apply gates
bell.h(0)
bell.cx(0, 1)

# Measure qubits
bell.measure([0, 1], [0, 1])

# Visualize circuit
bell.draw(output="mpl")

# Save your IBM Q account and load it (only need to save once)
IBMQ.save_account('36b1770273555e2252601dc0895db9670844228979de0798ce59cc99f4388c56602c7105510e3ec3ec10e471b05afec600779b983540dbe084f4d1c41708832d')  # Uncomment and replace 'YOUR_API_TOKEN' with your actual token if not saved yet
IBMQ.load_account()

# Use IBM Q provider and get the backend
provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_qasm_simulator')

# Transpile the circuit for the backend
t_qc = transpile(bell, backend=backend)

# Execute the quantum circuit on the backend
job = backend.run(t_qc)
job_monitor(job)  # This will show the job status in real-time

# Get the results and print them
result = job.result()
counts = result.get_counts(bell)
print(counts)


from qiskit.tools.visualization import plot_distribution
prob_distribution = job.result().quasi_dists[0].binary_probabilities()
plot_distribution(prob_distribution)

'''
import qiskit

#Sampler
from qiskit import QuantumCircuit

# Initialize quantum circuit
bell = QuantumCircuit(2,2)

# Apply gates
bell.h(0)
bell.cx(0,1)

# Measure qubits
bell.measure_all()

# Visualise circuit
bell.draw(output="mpl")


from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler
service = QiskitRuntimeService(channel="ibm_quantum",instance='ibm-q/open/main')

# Get the least busy backend, this step may take a while
simulator = "ibmq_qasm_simulator"
with Session(service, backend=simulator) as session:
    sampler = Sampler(session=session)
    job = sampler.run(bell)
    
# print job variable

'''