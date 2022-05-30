import numpy as np
from typing import Callable
from numpy import ndarray

def sigmoid(x:ndarray) -> ndarray:
    return 1/(1*np.exp(-x))

def deriv(func: Callable[[ndarray], ndarray], input_: ndarray, diff: float = 0.0001)-> ndarray:
    return(func(input_ + diff) - func(input_ - diff)) / (2*diff)


Array_Function = Callable[[ndarray], ndarray]

W = np.array([[1,1,1,1,1,1,1,1]])

X = np.array([[1,2,3,4,5,6,7,8]])

def matrix_function_backward_1(X: ndarray, W: ndarray,  sigma: Array_Function) -> ndarray:
	assert X.shape[1] == W.shape[0]
	N = np.dot(X, W)

	S = sigma(N)

	dSdN = deriv(sigma, N)

	dNdX = np.transpose(W, (1, 0))

	return np.dot(dSdN, dNdX)

print(matrix_function_backward_1(X, W, sigmoid))