# QUANTUM ALGORITHM: 
## QISKIT
### Sampler
This primitive takes circuits as input and returns a quasi-probability distribution over the measurement outcomes. This generalizes histograms from quantum circuits, allowing for mitigation of readout errors.

### Error Suppression / Mitigation
Qiskit Runtime's error suppression techniques + error mitigation techniques

## qaoa.py
This code will generate a QAOA quantum circuit based on the graph given (a triangle in this case). The depth of the QAOA circuit is specified by p.

This circuit is then transpiled and executed on IBM's quantum simulator. In a real-world scenario, optimizing the values of beta and gamma is essential for QAOA's success, typically done using classical optimization algorithms. This example just uses random values for demonstration purposes.