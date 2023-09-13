# QUANTUM ALGORITHM: 
## Evaluate efficiency of quantum circuit:
1. Number of quantum bits
2. Depth
3. Program execution speed (Runtime)
4. Number of Instructions

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

## Grover's Algorithm
Qiskit Implementation: Grover's Algorithm using two qubits

1. Initialization:
- Create a two-qubit quantum register and a two-bit classical register to store measurement results.

![2qubit](https://github.com/ilenhanako/HFC2023/assets/9971306/758a8120-401e-45db-81e6-e53553888e8c)

- Apply Hadamard gates to both qubits to initialize them in a superposition of all possible states.

2. Oracle Application:
- Integrate a quantum oracle that flags a specific state (or states) by adding a negative phase to it. 

3. Amplitude Amplification: "inversion about the average"
- amplifies the probability amplitude of the marked state. 
- In the two-qubit case, this typically involves applying more Hadamard gates and a series of other gates to shift the amplitudes.

![2qubit2](https://github.com/ilenhanako/HFC2023/assets/9971306/13fb2fd7-bf36-48a9-b69e-dff33c032ce1)

4. Measurement:
- Measure the two qubits, collapsing them to one of the possible states (00, 01, 10, or 11). After a few iterations of the algorithm (specifically, the oracle and amplitude amplification steps), the desired state (the one the oracle flags) should be measured with higher probability.
![2qubit3](https://github.com/ilenhanako/HFC2023/assets/9971306/42843b1e-6e45-4986-9f4e-ed720eec76de)

5. Visualization:
- Visualize the quantum circuit using the draw method

## Minimize Overfitting on Real-time Data
With growing nqubits the dependency on the number of layers is getting weaker.

It is shown for the MNIST data, how the training data's ACC depends on the number of layers; with the number of qubits in [2, 4, 8, 12].

Training Accuracy of MNIST data as a function of nqubits:
![no ofqubits](https://github.com/ilenhanako/HFC2023/assets/9971306/4c881aa0-b1e0-46a1-a57a-185a8f289129)

Training accuracy of MNIST data as a function of nlayers:
![no oflayers](https://github.com/ilenhanako/HFC2023/assets/9971306/576259f2-c54d-4122-b7b0-91c0854319b1)

1. Quantum Data Splitting:
Splitting your quantum data into training, validation, and test sets. Fine-tuning parameters (like angles in QAOA), you can optimize on the training set and validate on a separate quantum data validation set.

2. Limit the Depth in QAOA: p 
Increasing the depth (i.e., the number of layers) in QAOA can make the algorithm more expressive but might also increase the risk of overfitting, especially with noisy quantum hardware. Starting with a shallower circuit and then gradually increasing depth (while monitoring performance on validation data) can be a prudent strategy.

3. Noise Mitigation:
Overfitting in the quantum context can sometimes mean fitting to the noise of the quantum device rather than the underlying problem. Noise mitigation techniques, like zero noise extrapolation or error mitigation strategies, can help reduce the impact of device noise.
