from sklearn.metrics import mean_absolute_error


def get_error(Y_pred, Y_test):
    """
    This function is get the mean absolute error between the predicted label
    and the actual label

    :param Y_pred: The predicted labels from the regression model
    :param Y_test: The actual labels from the dataset
    :return: The mean absolute error value
    """
    return mean_absolute_error(Y_pred, Y_test)
