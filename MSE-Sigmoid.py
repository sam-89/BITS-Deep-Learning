import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Training data
x_values = [3, 4, 5, 6, 8]
actual_y_values = [0.268, 0.730, 0.952, 0.994, 0.999]

# Neuron parameters
w = 0.1
b = 0.1

# Predicted y values using the sigmoid function
predicted_y_values = [sigmoid(w*x + b) for x in x_values]

# Calculate Mean Squared Error (MSE)
mse = sum((predicted_y - actual_y) ** 2 for predicted_y, actual_y in zip(predicted_y_values, actual_y_values)) / len(x_values)

# Print the MSE rounded to 4 decimal places
print(f"Mean Squared Error (MSE): {mse:.4f}")
