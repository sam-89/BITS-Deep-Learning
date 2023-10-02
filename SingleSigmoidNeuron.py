#The input to the sigmoid function (also known as the activation function) in a neuron 
# is calculated as the sum of the element-wise multiplication of the input and weight vectors, 
# plus the bias. Here is a Python program that calculates this value:

import numpy as np  
  
# Given vectors  
X = np.array([0.1, 0.2, 0.3, 0.4])  
W = np.array([0.1, 0.2, 0.3, 0.4])  
  
# Given bias  
b = 0.15  
  
# Calculate input to the sigmoid function  
input_to_sigmoid = np.sum(W * X) + b  
  
print("Input to sigmoid Function is: ", input_to_sigmoid)  
