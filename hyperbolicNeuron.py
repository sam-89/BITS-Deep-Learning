import math

# Given values
x = 0.30
w = 0
b = 0.20
true_output = 0.10

# Calculate the predicted output using the hyperbolic tangent function
predicted_output = math.tanh(w * x + b)

# Calculate the Sum of Squared Errors (SSE)
sse = 0.5 * (true_output - predicted_output)**2

# Print the result
print(f"Approximate SSE: {sse:.4f}")
