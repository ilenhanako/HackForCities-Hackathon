# ERROR MITIGATION: Qiskit's Ignis Module

#...code for grover
# Importing Ignis error mitigation tools
from qiskit.ignis.mitigation.measurement import (complete_meas_cal, CompleteMeasFitter)

# Generate calibration circuits
meas_calibs, state_labels = complete_meas_cal(qr=qr, circlabel='mcal')

# Execute the calibration circuits
cal_job = execute(meas_calibs, backend=backend, shots=shots, optimization_level=0)
print(cal_job.job_id())
job_monitor(cal_job)
cal_results = cal_job.result()

# Fit the calibration results to construct a correction matrix
meas_fitter = CompleteMeasFitter(cal_results, state_labels, circlabel='mcal')
print(meas_fitter.cal_matrix)

# Get the filter object
meas_filter = meas_fitter.filter

# Apply the filter to the results from your Grover circuit
mitigated_results = meas_filter.apply(results)
mitigated_counts = mitigated_results.get_counts(groverCircuit)

# Plot the results
from qiskit.visualization import plot_histogram
plot_histogram([answer, mitigated_counts], legend=['raw', 'mitigated'])
