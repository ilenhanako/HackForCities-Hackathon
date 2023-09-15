# Hack for Cities 2023
QubitForce, for a "Quantum-centric Supercomputing for Smart Cities" competition

## Table of Contents:
1. dataProcessing1
- code for feature engineering of our inputs
- Loading datasests from cloud
- Transformation preprocessing: Check for stationarity in data 

2. QuantumAlgos
- errorM.py , Error mitigation techniques code for Grover
- grover.py , code for grover combined with errorM.pu
- qaoa.py , code for qaoa

3. qiskitsample.py
- initialization and implementation of qiskit

4. README_results.md
- Analyzing results of our algorithm with IBMQ

5. README_quantumalgos.md

## WHY QUANTUM????

1. Hybrid Quantum-Classical Ensembles:
Combining predictions from both quantum and classical algorithms could be beneficial. For example, certain problems might be solved more accurately with quantum algorithms, while others are more suited for classical algorithms.
This could involve running both a quantum algorithm and a classical algorithm on a given problem and then combining their outputs using a classical ensemble method, like voting or stacking.


2. Quantum Error Mitigation:
Noise and errors are significant issues in current quantum computers. While not an ensemble method in the traditional sense, techniques like Quantum Error Mitigation aim to correct the output of quantum algorithms by running them multiple times with slight variations, similar in spirit to bootstrapping in classical ensembles.


3. Diverse Quantum Algorithms:
One could run multiple quantum algorithms (or the same algorithm with different parameters or initializations) for a particular problem and combine their results, aiming to capture the strengths of each.


4. Parameter Ensembles:
Quantum algorithms often involve variational circuits with tunable parameters. Running the algorithm with different parameter initializations and aggregating the results could boost performance.



Stacking (Stacked Generalization):
Multiple models (or different configurations of the same model) are trained, and their predictions are combined using another model (meta-model) to make a final prediction.
HOW TO STACK FOR QUANTUM ALGO???