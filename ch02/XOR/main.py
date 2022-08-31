import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    theta = 1.0
    if x[0] * w[0] + x[1] * w[1] >= theta:
        return 1
    else:
        return 0

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    theta = 1.0
    if x[0] * w[0] + x[1] * w[1] >= theta:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1.0, 1.0])
    theta = 1.0
    if x[0] * w[0] + x[1] * w[1] >= theta:
        return 1
    else:
        return 0

for i in range(2):
    for j in range(2):
        print(AND(NAND(i, j), OR(i, j)))
