from sklearn.model_selection import train_test_split


def clean_data(X):
    """
    This function is used to clean the data in the dataset

    :param X: the dataframe containing the features of the datapoints
    :return: the dataframe with the clean, processed values of the features
    """
    X_cleaned = []
    for i in X:
        X_cleaned.append([i[0], i[1], i[2].timestamp(), i[3], i[4].timestamp(), i[5]])
    return X_cleaned


def clean_labels(Y):
    """
    This function is used to clean the labels in the dataset

    :param Y: the array containing the labels of the datapoints
    :return: the array of cleaned labels of the datapoints
    """
    Y_cleaned = []
    for i in range(Y.shape[0]):
        Y_cleaned.append([Y.iloc[i][0].total_seconds()])
    return Y_cleaned


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
