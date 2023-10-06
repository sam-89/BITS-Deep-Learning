import numpy as np
import sys
sys.getdefaultencoding()
sys.stdout.reconfigure(encoding='utf-8')

  
# Given vectors  
X = np.array([0.1, 0.2, 0.3, 0.4])  
W = np.array([0.4, 0.3, 0.2, 0.1])  
  
# Calculate summation of element-wise multiplication  
result = np.sum(W * X)  
  
print("\u03A3WX =", result)