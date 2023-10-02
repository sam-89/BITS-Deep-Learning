import numpy as np  
  
# Given vectors  
X = np.array([1.0, 2.0, 3.0, 4.0])  
W = np.array([0.4, 0.3, 0.2, 0.1])  
  
# Calculate summation of element-wise multiplication  
result = np.sum(W * X)  
  
print(result)