import numpy as np
from prettytable import PrettyTable


  
# Initialize weights and learning rate  
weights = np.array([-1.0, -2.0, -100])  
#learning_rate = 0.1  
  
# Given data and labels
x1 = np.array([7.50, 10.00, 5.00, 7.50, 15.00, 12.50, 17.50])  
x2 = np.array([10.00, 5.00, 15.00, 20.00, 12.50, 17.50, 15.00])
x0 = np.array([ 1.0,    1.0,   1.0,     1.0,   1.0,     1.0,   1.0])

X = np.array(list(zip(x1, x2, x0)))  
y = np.array([0, 0, 0, 0, 1, 1, 1])
  
for epoch in range(10):  # Number of Iterations will break if convergence is achieved
    old_weight = weights
    table = PrettyTable()
    table.field_names = ["", "w", "x"]
    print(f"Epoch {epoch+1}" )  
    for i in range(X.shape[0]):
        print("value of y",i+1, "is: ", y[i]) 
        #Compute the output prediction  
        output = np.dot(X[i], weights)  
        prediction = 1.0 if output > 0 else 0.0
        
        #print(weights, X[i], output)
        
        table.add_row([" ", weights[0], x1[i]])  
        table.add_row([" ", weights[1], x2[i]])  
        table.add_row([" ", weights[2], x0[i]])
        table.add_row(["w.x", output, " "])
        print(table)
        
        if prediction == 0 and y[i] == 1:
            print("y value is 1 and prediction is -ve : so need to update weights: = w+x")  
            # Update weights  
            weights = weights + X[i]
            print("New weights: ", weights)
        elif prediction == 0 and y[i] == 0:
            print("y value is 0 and prediction is also -ve, so no update weights.")
        elif prediction == 1 and y[i] == 0:
            print("y value is 0 but prediction is +ve, so need update of weights: = w-x")
            weights = weights - X[i]
            print("New weights: ", weights)
        else:
            print("y value is +ve and prediction is also +ve, so no update of weights")
     
    print(weights)
    print(old_weight)
    compare_weight = old_weight == weights
    if compare_weight.all():
        print("Convergence is achieved")
        break
    else:
        print("Convergence not achieved yet")
    