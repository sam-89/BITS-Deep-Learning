import math
import sys
sys.getdefaultencoding()
sys.stdout.reconfigure(encoding='utf-8')


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def g_sigmoid(x):
    sigma_x = sigmoid(x)
    result = math.log((1 - sigma_x) / sigma_x)
    return result

# Example usage:
x_value = 2.0
result_g_sigmoid = g_sigmoid(x_value)

print(f"The value of g(σ({x_value})) is: {result_g_sigmoid}")


