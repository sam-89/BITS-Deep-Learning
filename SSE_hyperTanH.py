import numpy as np

# Given values
x = 0.30
w = 0
b = 0.2
y_true = 0.10

# Calculate the predicted output
y_predicted = np.tanh(w * x + b)

# Calculate the Sum of Squared Errors (SSE)
sse = (y_true - y_predicted)**2

print(f"The predicted output is: {y_predicted}")
print(f"The Sum of Squared Errors (SSE) is approximately: {sse}")
