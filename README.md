# Hack for Cities 2023
"Quantum-centric Supercomputing for Smart Cities"
## Traffic Prediction Dataset
[Traffic Prediction: Custom, GRU, LSTM, CNN, MLP](https://www.kaggle.com/code/atulchoudhary29/traffic-prediction-custom-gru-lstm-cnn-mlp/input)

- Number of instances = 48120
- DateTime = datetime in hourly frequency
- Junction = number of junctions on road
- Vehicles = number of vehicles at that hour
- ID number of vehicles

## Step 1e: Feature Extraction
[From EDA to the Top](https://www.kaggle.com/code/gaborfodor/from-eda-to-the-top-lb-0-367)
model used to predict the total ride duration of taxi trips in NYC
- Dataset: 2016 NYC Yellow Cab trip record data (available on Big Query on Google Cloud Platform)

1. PCA, used to transform longitude and latitude coordinates. No dimension reduction as it is a transformation from 2D --> 2D
- The rotation could help for decision tree splits.

2. Distance, calculate distance between pickup and dropoff points
- using Haversine function(distance formula), more info on [Haversine code](https://www.kaggle.com/code/jpmiller/vincenty-haversine-euclidean-they-can-all-work)
- other options: geopy has another heuristics (vincenty() or great_circle())

3. DateTime features
- done by previous kaggle notebook

4. Speed, rush hour average traffic speed

5. Cluster analysis, to analyse recurrent network flow patterns 
- Study on [Cluster analysis](https://www.sciencedirect.com/science/article/pii/S0968090X22002959#:~:text=Cluster%20analysis%20(or%20clustering)%20for,a%20long%20period%20of%20time.)

## QUANTUM ALGORITHM: QISKIT
### Sampler
This primitive takes circuits as input and returns a quasi-probability distribution over the measurement outcomes. This generalizes histograms from quantum circuits, allowing for mitigation of readout errors.

### Error Suppression / Mitigation
Qiskit Runtime's error suppression techniques + error mitigation techniques

## qaoa.py
This code will generate a QAOA quantum circuit based on the graph given (a triangle in this case). The depth of the QAOA circuit is specified by p.

This circuit is then transpiled and executed on IBM's quantum simulator. In a real-world scenario, optimizing the values of beta and gamma is essential for QAOA's success, typically done using classical optimization algorithms. This example just uses random values for demonstration purposes.