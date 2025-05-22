import numpy as np
print(np.__version__)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([
    [0],
    [1],
    [1],
    [0]
])
np.random.seed(0)
input_layer_size = 2
hidden_layer_size = 4
output_layer_size = 1
learning_rate = 0.1
epochs = 10000
W1 = np.random.randn(input_layer_size, hidden_layer_size)
b1 = np.zeros((1, hidden_layer_size))
W2 = np.random.randn(hidden_layer_size, output_layer_size)
b2 = np.zeros((1, output_layer_size))
for epoch in range(epochs):
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)
    loss = np.mean((y - a2) ** 2)
    d2 = (y - a2) * sigmoid_derivative(a2)
    d1 = np.dot(d2, W2.T) * sigmoid_derivative(a1)
    W2 += np.dot(a1.T, d2) * learning_rate
    b2 += np.sum(d2, axis=0, keepdims=True) * learning_rate
    W1 += np.dot(X.T, d1) * learning_rate
    b1 += np.sum(d1, axis=0, keepdims=True) * learning_rate
    if epoch % 1000 == 0:
        print(f"Epoch {epoch} | Loss: {loss:.4f}")
print("\nFinal Predictions:")
print(np.round(a2, 3))
