import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

print(softmax(np.array([1010, 1000, 990]))) # 오버플로우 문제

def newSoftmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

print(newSoftmax(np.array([1010, 1000, 990]))) # 오버플로우 문제 해결
