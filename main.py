from config import config
from connect_database import connect_and_fetch_data
import pandas as pd
import numpy as np
from data_pre_processing import *
from regression_model import *
from error_analysis import *
from plot_results import *


if __name__ == '__main__':

    # read connection parameters
    params = config()

    # fetch column names from database
    query = "SELECT column_name from INFORMATION_SCHEMA.columns where table_name = 'final_table3'"
    cols = connect_and_fetch_data(query, params)
    print("Column names: ", cols)

    # fetch data from database
    X_query = "SELECT snapshot_count, total_targets, original_date, num_revision, last_revision, num_releases " \
            "FROM final_table3"
    X_list = connect_and_fetch_data(X_query, params)

    # fetch labels from database
    Y_query = "SELECT lifespan from final_table3"
    Y_list = connect_and_fetch_data(Y_query, params)

    # convert data list to dataframe
    X = pd.DataFrame.from_records(X_list, columns=['snapshot_count', 'total_targets', 'original_date',
                                                   'num_revision', 'last_revision', 'num_releases'])
    Y = pd.DataFrame.from_records(Y_list, columns = ['lifespan'])
    X = X.values

    # data pre-processing
    X = clean_data(X)
    X = np.array(X)
    Y = clean_labels(Y)
    Y = np.divide(Y, 86400) # convert to days
    X_train, X_test, Y_train, Y_test = split_train_test(X, Y)

    # regression model
    model = regression_model_fit(X_train, Y_train)
    avg_value = np.average(Y_train)
    Y_predict = regression_model_predict(X_test, model)
    Y_average = np.full(Y_predict.shape, avg_value)

    # error analysis
    regression_error = get_error(Y_predict, Y_test)
    random_error = get_error(Y_average, Y_test)
    print("Error by regression: ", regression_error)
    print("Error by average (baseline): ", random_error)

    # plotting the results
    plot(X_test[:, 0], Y_test, Y_predict, Y_average, "snapshot count", "Lifespan (in days)", "Predict Lifespan from snapshot count")
    plot(X_test[:, 1], Y_test, Y_predict, Y_average, "total targets", "Lifespan (in days)", "Predict Lifespan from number of targets")
    plot(X_test[:, 2], Y_test, Y_predict, Y_average, "original date", "Lifespan (in days)", "Predict Lifespan from original date")
    plot(X_test[:, 3], Y_test, Y_predict, Y_average, "revision count", "Lifespan (in days)", "Predict Lifespan from number of revisions")
    plot(X_test[:, 4], Y_test, Y_predict, Y_average, "last revision", "Lifespan (in days)", "Predict Lifespan from last revision date")
    plot(X_test[:, 5], Y_test, Y_predict, Y_average, "releases count", "Lifespan (in days)", "Predict Lifespan from number of releases")

