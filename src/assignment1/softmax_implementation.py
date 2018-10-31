import numpy as np


def softmax(x):
    exp_x = np.exp(x)
    sm_x = exp_x / np.sum(exp_x)
    return sm_x


a = [11, 4, 5, 8]
b = softmax(a)
print(b)