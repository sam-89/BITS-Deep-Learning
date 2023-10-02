import numpy as np  
  
# Given data  
x = np.array([3, 4, 5, 6, 8])  
y_true = np.array([0.268, 0.730, 0.952, 0.994, 0.999])  
  
# Initialize weights  
w = b = 1
  
# Calculate output  
y_pred = np.tanh(w * x + b)  
  
# Calculate MSE  
mse = np.mean((y_true - y_pred)**2)

print(mse)