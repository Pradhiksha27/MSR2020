import matplotlib.pyplot as plt


# Visualising the Train and test set results
def plot(X, Y, Y_predicted, Y_baseline, X_label, Y_label, title):
    """
    This function plots the graph, given the data values

    :param X: the feature value array to be plotted on X-axis
    :param Y: the true label value array to be plotted on Y-axis
    :param Y_predicted: the predicted label value array to be plotted on Y-axis
    :param Y_baseline: the baseline label value array to be plotted on Y-axis
    :param X_label: The label name to be used for X-axis
    :param Y_label: The label name to be used for Y-axis
    :param title: The title of the plot
    :return: None
    """
    plt.scatter(X, Y, color = 'black', label="Actual value")
    plt.scatter(X, Y_predicted, color = 'blue', label = "Regressor predicted value")
    plt.scatter(X, Y_baseline, color = 'red', label = "Baseline average value")

    plt.title(title)
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.legend()

    plt.show()
