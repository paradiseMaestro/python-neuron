import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
inputs = np.array([0,0,1]) # 3 входа на 3 нейрона
weights = np.array([10,0,-5])# 3 веса 
outputs = sigmoid(np.dot(inputs,weights)) # работа выходного нейрона
print(outputs)