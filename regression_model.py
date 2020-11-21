from sklearn.linear_model import LinearRegression


def regression_model_fit(X, Y, model=LinearRegression()):
    """
    This function is used to fit the provided model with the training dataset provided

    :param X: the feature set of the datapoints for regression prediction
    :param Y: the labels of the datapoints
    :param model: The regression model to be used
    :return: the fitted regression model
    """
    regressor = model
    regressor.fit(X, Y)
    return regressor


def regression_model_predict(X, model):
    """
    This function is used to predict the labels for the test dataset provided

    :param X: The feature set for which the prediction is to be made
    :param model: The regression model used for the result
    :return: The Y labels predicted by the model
    """
    return model.predict(X)
