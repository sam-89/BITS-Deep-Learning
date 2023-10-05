import math

# Given vectors
v1 = [4, 5]
v2 = [-3, -4]

# Calculate dot product
dot_product = sum(x * y for x, y in zip(v1, v2))

# Calculate magnitudes
magnitude_v1 = math.sqrt(sum(x**2 for x in v1))
magnitude_v2 = math.sqrt(sum(x**2 for x in v2))

# Calculate the angle in radians
angle_radians = math.acos(dot_product / (magnitude_v1 * magnitude_v2))

# Convert angle to degrees
angle_degrees = math.degrees(angle_radians)

# Print the result
print(f"The angle between v1 and v2 is approximately {angle_degrees:.2f} degrees.")
