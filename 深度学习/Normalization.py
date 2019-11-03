# BN
import numpy as np
'''
x.shape [N, C, H, W]
'''
def BN(x, gamma, beta, eps = 10e-6):
    x_mean = np.mean(x, axis = (0, 2, 3), keepdims = True)
    x_var = np.var(x, axis = (0, 2, 3), keepdims = True)
    x_norm = (x - x_mean) / np.sqrt(x_var + eps)
    x_norm =  gamma * x_norm + beta 
    return x_norm

# LN 
def LN(x, gamma, beta, eps = 10e-6):
    x_mean = np.mean(x, axis = (1, 2, 3), keepdims=True)
    x_var = np.var(x, axis = (1, 2, 3), keepdims=True)
    x_norm = (x - x_mean) / np.sqrt(x_var + eps)
    x_norm =  gamma * x_norm + beta 
    return x_norm


# IN 
def IN(x, gamma, beta, eps = 10e-6):
    x_mean = np.mean(x, axis = (2, 3), keepdims=True)
    x_var = np.var(x, axis = (2, 3), keepdims=True)
    x_norm = (x - x_mean) / np.sqrt(x_var + eps)
    x_norm =  gamma * x_norm + beta 
    return x_norm

# GN 
def GN(x, gamma, beta, G, eps = 10e-6):
    x = np.reshape(x, (x.shape[0], G, x.shape[1] // G, x.shape[2], x.shape[3]))
    x_mean = np.mean(x, axis = (2, 3, 4), keepdims=True)
    x_var = np.var(x, axis = (2, 3, 4), keepdims=True)
    x_norm = (x - x_mean) / np.sqrt(x_var + eps)
    x_norm =  gamma * x_norm + beta 
    return x_norm