import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def clean_data(X):
    X_cleaned = []
    for i in X:
        X_cleaned.append([i[0], i[1], i[2].timestamp(), i[3], i[4].timestamp(), i[5]])
    return X_cleaned


def split_train_test(X, Y, ratio=0.3):
    """
    This function is used to split the dataset into training and testing dataset

    :param X: the feature set of the datapoints for regression prediction
    :param Y: the labels of the datapoints
    :param ratio: the test dataset ratio
    :return: the training and testing datasets
    """
    # Splitting the dataset into the Training set and Test set
    return train_test_split(X, Y, test_size = ratio, random_state = 0)


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

def get_error(Y_pred, Y_test):
    """
    This function is get the mean absolute error between the predicted label
    and the actual label

    :param Y_pred: The predicted labels from the regression model
    :param Y_test: The actual labels from the dataset
    :return: The mean absolute error value
    """
    return mean_absolute_error(Y_pred, Y_test)


# Visualising the Train and test set results
def plot(X, Y, Y_predicted, X_label, Y_label, title):
    """
    This function plots the graph

    :return: None
    """
    # print(X.shape, Y.shape, Y_predicted.shape)
    plt.scatter(X, Y, color = 'black', label="actual value")
    plt.scatter(X, Y_predicted, color = 'blue', label = "predicted value")
    # plt.scatter(X_Test, Y_Test, color = 'green')
    # plt.plot(X_Train, regressor.predict(X_Train), color = 'red', label = "testing")
    plt.title(title)
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.legend()
    plt.show()
