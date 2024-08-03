import numpy as np

# Sigmoid function to normalize inputs
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function for backpropagation
def sigmoid_derivative(x):
    return x * (1 - x)

# Training dataset
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

# Initialize weights with random values
np.random.seed(1)
weights = 2 * np.random.random((3, 1)) - 1

# Train the neural network
for iteration in range(20000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, weights))
    
    # Calculate the error
    error = training_outputs - outputs
    
    # Multiply error by input and gradient of the sigmoid function
    adjustments = error * sigmoid_derivative(outputs)
    
    # Adjust weights
    weights += np.dot(input_layer.T, adjustments)

print('Trained weights after 20,000 iterations:')
print(weights)

# Test the network with a new situation
new_inputs = np.array([1, 0, 0])
output = sigmoid(np.dot(new_inputs, weights))
print("New situation [1, 0, 0] -> New Output:")
print(output)
