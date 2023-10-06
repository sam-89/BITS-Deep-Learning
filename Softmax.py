import numpy as np

# Given vector
z = np.array([0.6, 1.1, -0.6])

# Softmax function
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Subtracting max(x) for numerical stability
    return exp_x / np.sum(exp_x)

# Apply softmax to the vector
softmax_output = softmax(z)

# Print the result
print("Softmax output:", softmax_output)
