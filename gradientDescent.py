import numpy as np

# Given data
x = np.array([3.000, 4.250, 4.500, 4.900, 5.500, 6.100])
y = np.array([0.018, 0.182, 0.269, 0.450, 0.731, 0.900])

# Initial parameters
w = 2
b = -8
learning_rate = 0.25
epochs = 10  # Number of training iterations

# Sigmoid activation function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Mean Squared Error (MSE) loss function
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# Training the model using Gradient Descent
for epoch in range(epochs):
    # Forward pass
    z = w * x + b
    y_pred = sigmoid(z)

    # Compute the gradient of the loss with respect to y_pred
    dy_pred = 2 * (y_pred - y)

    # Compute the gradient of the sigmoid function
    dz = y_pred * (1 - y_pred)

    # Backward pass - Compute the gradients for weights and bias
    dw = np.dot(dy_pred * dz, x)
    db = np.sum(dy_pred * dz)

    # Update weights and bias
    w -= learning_rate * dw
    b -= learning_rate * db

    # Calculate and print both MSE and SSE
    mse = mse_loss(y, y_pred)
    sse = mse * len(y)  # SSE is MSE multiplied by the number of data points
    print(f"After iteration {epoch + 1}, MSE: {mse:.6f}, SSE: {sse:.6f}")

# Print the final weights and bias
print("Final Weights:", w)
print("Final Bias:", b)
