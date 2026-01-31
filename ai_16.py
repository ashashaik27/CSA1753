import numpy as np

# Activation functions
def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)

# Feed Forward Neural Network class
class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size, lr=0.01):
        self.lr = lr
        
        # Initialize weights & biases
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))

        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))
        
    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = relu(self.z1)
        
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2
    
    def backward(self, X, y):
        m = X.shape[0]
        
        dz2 = (self.a2 - y) * sigmoid_derivative(self.z2)
        dW2 = (self.a1.T @ dz2) / m
        db2 = np.sum(dz2, axis=0, keepdims=True)

        dz1 = (dz2 @ self.W2.T) * relu_derivative(self.z1)
        dW1 = (X.T @ dz1) / m
        db1 = np.sum(dz1, axis=0, keepdims=True)

        # gradient descent
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        
    def train(self, X, y, epochs=1000):
        for ep in range(epochs):
            self.forward(X)
            self.backward(X, y)
            if ep % 100 == 0:
                loss = np.mean((self.a2 - y) ** 2)
                print(f"Epoch {ep}, Loss = {loss:.4f}")

# Example usage
X = np.array([[0,0],[0,1],[1,0],[1,1]])   # XOR input
y = np.array([[0],[1],[1],[0]])           # XOR output

model = FeedForwardNN(input_size=2, hidden_size=3, output_size=1, lr=0.1)
model.train(X, y, epochs=2000)

print("Predictions:")
print(model.forward(X))
