# Hack for Cities 2023
QubitForce, for a "Quantum-centric Supercomputing for Smart Cities" competition

[Link to our technical flowchart](https://www.canva.com/design/DAFtgmUGEhI/1p6rIi220_9FIIAJnlQx4Q/edit?utm_content=DAFtgmUGEhI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

[Link to our final presentation slides](https://www.canva.com/design/DAFuRvF0jII/T86rOhQR113hUjc3HHFTKw/edit?utm_content=DAFuRvF0jII&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

[Link to our final report](https://github.com/Avitra2002/HackForCities-Hackathon/files/13792220/FINAL.report.docx.pdf)


## Meet the Team:

<img width="692" alt="Screenshot 2023-09-15 at 4 08 24 PM" src="https://github.com/ilenhanako/HFC2023/assets/9971306/f4ca1535-5784-4630-9451-f47ec198afc6">

## Project Overview
QubitForce tackles the critical challenge of traffic congestion in smart cities. Our project leverages the power of quantum computing to address issues like inflexible lane configurations and under-optimized road infrastructure, revolutionizing urban traffic management.

### Challenges:
Inflexible Lane Configurations: Traditional traffic systems lack the flexibility to adapt to varying traffic conditions.
Under-Optimized Road Infrastructure: Existing infrastructure often fails to maximize efficiency, leading to increased congestion.

**Our Quantum Approach:**
QubitForce introduces an innovative approach to manage urban traffic congestion. Our solution harnesses the power of quantum computing, integrating sophisticated algorithms like Grover’s Search, QAOA, and Quantum Walk. This framework enables dynamic analysis and optimization of traffic flow, addressing challenges like inflexible lane configurations and under-optimized road infrastructure. By parallelizing these quantum algorithms and incorporating classical machine learning, we offer real-time, scalable solutions for urban traffic management. Our hybrid quantum-classical ensemble ensures efficient data processing, optimal lane usage, and dynamic traffic control strategies, paving the way for smarter, congestion-free cities.

## Table of Contents:
1. dataProcessing1
- code for feature engineering of our inputs
- Loading datasests from cloud
- Transformation preprocessing: Check for stationarity in data 

2. QuantumAlgos
- errorM.py , Error mitigation techniques code for Grover
- grover.py , Code for grover combined with errorM.pu
- qaoa.py , Code for qaoa

3. qiskitsample.py
- Initialization and implementation of qiskit

4. README_results.md
- Analyzing results of our algorithm with IBMQ

5. README_quantumalgos.md

## Why did we choose Quantum Computing?

1. Hybrid Quantum-Classical Ensembles: This approach effectively tackles the dynamic nature of urban traffic. Quantum algorithms can rapidly process complex scenarios like variable traffic patterns, while classical algorithms can handle more predictable aspects, leading to a comprehensive traffic management system.

2. Quantum Error Mitigation: In the context of traffic management, this means more reliable predictions and optimization strategies in real-time, crucial for managing unpredictable traffic flows.

3. Diverse Quantum Algorithms: Different quantum algorithms can be employed to address various facets of the traffic problem – from optimizing traffic flow at intersections to adjusting lane configurations – providing a multi-faceted solution.

4. Parameter Ensembles in Quantum Algorithms: By running these algorithms with varied parameters, the solution can adapt to different traffic conditions, ensuring optimal traffic management under various scenarios.


Stacking (Stacked Generalization):
Multiple models (or different configurations of the same model) are trained, and their predictions are combined using another model (meta-model) to make a final prediction.
HOW TO STACK FOR QUANTUM ALGO???
