import sympy as sp

# Define the variable x as a symbol
x = sp.symbols('x')

# Define the function y
y = (1 + sp.exp(-x)) / (1 - sp.exp(-x))

# Take the order of the derivative as input
order = int(input("Enter the order of the derivative: "))

# Define the value of x
specific_x_value = 4

# Calculate the nth-order derivative of y with respect to x
derivative_result = sp.diff(y, x, order)

# Substitute the specific value of x into the derivative expression
derivative_result_at_specific_x = derivative_result.subs(x, specific_x_value)

# Evaluate the expression to get a numeric result
derivative_numeric_result = derivative_result_at_specific_x.evalf()

# Print the result
print(f"{order}th-order derivative at x = {specific_x_value}:")
print(derivative_numeric_result)
