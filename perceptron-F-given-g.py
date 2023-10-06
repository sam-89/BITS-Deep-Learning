# Given values
X = [0.1, 0.2, 0.3, 0.4]
W = [0.1, 0.2, 0.3, 0.4]
b = 0.15

# Calculate the weighted sum plus bias
g = sum(xi * wi for xi, wi in zip(X, W)) + b

print("The input to the f part (g) of the perceptron is:", g)
