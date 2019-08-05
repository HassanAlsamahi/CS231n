from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

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
    num_train = X.shape[0]
    num_classes = W.shape[1]
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################

    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    for i in range(0,num_train):
        scores = X[i].dot(W)
        scores -= scores.max()
        correct = scores[y[i]]

        correct_exp = np.exp(correct)
        scores_exp = np.exp(scores)
        exp_sum = np.sum(scores_exp)

        loss_i = - np.log(correct_exp/exp_sum)
        loss += loss_i

        for j in range(num_classes):
            if j == y[i]:
                dW[:,j] -= (1 - (correct_exp/exp_sum)) * X[i]

            else:
                dW[:, j] -= 0 - (scores_exp[j] / exp_sum) * X[i]

    loss /= num_train
    loss += reg * np.sum(W*W)

    dW /= num_train
    dW += 2*reg*W

    pass
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
    num_train = X.shape[0]
    num_classes = W.shape[1]

    scores = X.dot(W)
    scores -= np.max(scores)
    exps = np.exp(scores)
    correct = scores[np.arange(num_train),y]
    correct_exp = np.exp(correct)
    exps_sum = np.sum(exps,axis=1)
    loss = -np.log(correct_exp/exps_sum)
    loss = np.sum(loss)
    loss /= num_train
    loss += reg*np.sum(W*W)

    exps_sum = np.expand_dims(exps_sum,axis=1)
    mult = exps/exps_sum
    mult[np.arange(num_train),y] -= 1
    dW = X.T.dot(mult)
    dW /= num_train
    dW += 2*reg*W


    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
