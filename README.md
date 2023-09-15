# Hack for Cities 2023
QubitForce, for a "Quantum-centric Supercomputing for Smart Cities" competition

[Link to our technical flowchart](https://www.canva.com/design/DAFtgmUGEhI/1p6rIi220_9FIIAJnlQx4Q/edit?utm_content=DAFtgmUGEhI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

[Link to our final presentation slides](https://www.canva.com/design/DAFuRvF0jII/T86rOhQR113hUjc3HHFTKw/edit?utm_content=DAFuRvF0jII&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Meet the Team:

<img width="692" alt="Screenshot 2023-09-15 at 4 08 24 PM" src="https://github.com/ilenhanako/HFC2023/assets/9971306/f4ca1535-5784-4630-9451-f47ec198afc6">

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
