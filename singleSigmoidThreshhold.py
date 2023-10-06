import math

# Given inputs and weights
x = [0.1, 0.2, 0.3]
weights = [0.1, 0.2, 0.3]
threshold = 0.1

# Calculate the weighted sum and add the threshold
weighted_sum = sum(xi * wi for xi, wi in zip(x, weights)) + threshold

# Calculate the sigmoid activation function
output = 1 / (1 + math.exp(-weighted_sum))

# Print the result
print(f"The approximate output of the sigmoid neuron is: {output:.4f}")
