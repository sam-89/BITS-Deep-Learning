from scipy.optimize import fsolve
import math

# Given values
w = 0.2
b = 0.3
desired_output = 0.60

# Sigmoid function
sigmoid = lambda x: 1 / (1 + math.exp(-(w*x + b)))

# Define the equation to be solved
equation = lambda x: sigmoid(x) - desired_output

# Use fsolve to find the solution numerically
initial_guess = 0  # Initial guess for x
solution = fsolve(equation, initial_guess)

print("The value of x for which the sigmoid function yields 0.60 is approximately:", solution[0])
