import numpy as np

def stablesoftmax(z):
    D = np.max(z)
    shift = z - D
    exp = np.exp(shift)
    return exp / np.sum(exp)

def softmaxloss(W, X, y, reg):
    """
    输入样本维度是D，有C类，batchsize是N  [D, C, N]

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
 """

    loss = 0.0
    dW = np.zeros_like(W)
    nums_train = X.shape[0]
    nums_class = X.shape[1]
    # 前向
    Z = X.dot(W)
    shiftZ = Z - np.max(Z, axis = 1).reshape(-1, 1)
    softmax = np.exp(shiftZ) / np.sum(np.exp(shiftZ), axis = 1).reshape(-1, 1)
    loss = -np.sum(np.log(softmax[range(nums_train), list(y)]))
    loss /= nums_train
    loss += 0.5 * reg * np.sum(W * W)
    # 反向
    dz = softmax.copy()
    dz[range(num_train), list(y)] += -1
    dW = (X.T).dot(dz)
    dW = dW / nums_train + reg * W  

    return loss, dW




