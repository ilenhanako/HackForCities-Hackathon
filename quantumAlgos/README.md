# QUANTUM ALGORITHM: 
## QISKIT
### Sampler
This primitive takes circuits as input and returns a quasi-probability distribution over the measurement outcomes. This generalizes histograms from quantum circuits, allowing for mitigation of readout errors.

### Error Suppression / Mitigation
Qiskit Runtime's error suppression techniques + error mitigation techniques

## qaoa.py
This code will generate a QAOA quantum circuit based on the graph given (a triangle in this case). The depth of the QAOA circuit is specified by p.

This circuit is then transpiled and executed on IBM's quantum simulator. In a real-world scenario, optimizing the values of beta and gamma is essential for QAOA's success, typically done using classical optimization algorithms. This example just uses random values for demonstration purposes.

### QAOA Circuit Definition:

The qaoa_circuit function is designed to create a quantum circuit implementing the QAOA algorithm.

The function takes as input:

- graph: which defines the problem (connections between qubits).
- p: the number of QAOA layers.
- beta and gamma: angles that parameterize the circuit.
- The function starts with an initial state preparation where every qubit is put into a superposition using Hadamard gates.

#### For each QAOA layer (p layers):
- Problem unitary: Using RZZ and RXX gates, it encodes the problem we are trying to solve with QAOA.
- Mixer unitary: Using single-qubit rotations (RX, RY, RZ), it changes the quantum state in a manner dictated by the angles beta and gamma.

In essence, this code sets up a parameterized quantum circuit using the QAOA algorithm and then runs this circuit on an IBM quantum simulator. The results returned represent the probabilities of each quantum state after the QAOA algorithm has been executed, and the goal in a typical QAOA problem would be to use these results (along with classical optimization) to find an optimal or near-optimal solution to the problem represented by the input graph.