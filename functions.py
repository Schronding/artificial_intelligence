import matplotlib.pyplot as plt
import numpy as np

beginning = -10
end = 10

X = np.linspace(beginning, end, 100)
# np.arange by defect uses jumps of 1, while np.linspace breaks the range between your array by how many 
# values do you want. 

def Sigmoid(array):
    return 1/ (1 + np.exp(-array))

def SoftPlus(array):
    return np.log(1 + np.exp(array))

Y = Sigmoid(X)
Z = SoftPlus(X)

plt.plot(X, Y)
plt.show()
plt.plot(X, Z)
plt.show()