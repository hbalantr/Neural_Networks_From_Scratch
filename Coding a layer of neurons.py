# Coding a layer of neurons 
import numpy as np
inputs = [1,2,3,2.5]
weights = [[0.2,0.8,-0.5,1],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
bias1 = 2
bias2 = 3
bias3 = 0.5
outputs = [[weights[0][0]*inputs[0]+ weights[0][1]*inputs[1]+weights[0][2]*inputs[2]+weights[0][3]*inputs[3]+bias1],[weights[1][0]*inputs[0]+ weights[1][1]*inputs[1]+weights[1][2]*inputs[2]+weights[1][3]*inputs[3]+bias2],[weights[2][0]*inputs[0]+ weights[2][1]*inputs[1]+weights[2][2]*inputs[2]+weights[2][3]*inputs[3]+bias3]]
print(outputs)


# If we use loops it will be use. As we know to code for 50 neurons we cant keep on coding every neuron. So we have to use loops. 
# 2- Problem
inputs = [1,2,3,2.5] 
weights = [[0.2,0.8,-0.5,1],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

outputs = []

for neuron_weights, neuron_biases in zip(weights,biases):
    neuron_output = 0
    for neuron_inputs, neuron_weights in zip(inputs,neuron_weights):
        neuron_output += neuron_inputs*neuron_weights
        
    neuron_output += neuron_biases
    outputs.append(neuron_output)
print(outputs)
   

#The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. Each tuple contains elements from the input iterables that are at the same position.


# Coding it using numpy 

outputs_new = [np.dot(inputs,weights[0])+biases[0],np.dot(inputs,weights[1])+biases[1],np.dot(inputs,weights[2])+biases[2]]
print(outputs_new)
outputs_1 = np.dot(weights,inputs)+biases
print(outputs_1)