def gradient_descent_update(x, gradx, learning_rate):
    """
    Performs a gradient descent update.
    """
    return x - (learning_rate * gradx)
