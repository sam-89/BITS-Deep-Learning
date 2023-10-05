# Given points
x1, y1 = 3, 4
x2, y2 = 5, 6

# Calculate the slope (m)
slope = (y2 - y1) / (x2 - x1)

# Use the point-slope form to find the equation of the line
# y - y1 = m(x - x1)
equation = f"y - {y1} = {slope}(x - {x1})"

print(f"The equation of the line is: {equation}")

# Simplify the equation to slope-intercept form
equation_simplified = f"y = {slope}x + {y1 - slope * x1}"

print(f"Simplified equation: {equation_simplified}")
