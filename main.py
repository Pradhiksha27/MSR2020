from config import config
from connect_database import connect_and_fetch_data
from get_stats import get_stats
import pandas as pd
from regression_model import *

if __name__ == '__main__':
    # read connection parameters
    params = config()

    # query for the database
    query = "SELECT column_name from INFORMATION_SCHEMA.columns where table_name = 'final_table3'"
    # fetch data from database
    cols = connect_and_fetch_data(query, params)
    print("Column names: ", cols)

    X_query = "SELECT snapshot_count, total_targets, original_date, num_revision, last_revision, num_releases " \
            "FROM final_table3"
    # fetch data from database
    X_list = connect_and_fetch_data(X_query, params)
    # get statistics
    get_stats(X_list)
    Y_query = "SELECT lifespan from final_table3"
    # fetch data from database
    Y_list = connect_and_fetch_data(Y_query, params)

    X = pd.DataFrame.from_records(X_list, columns=['snapshot_count', 'total_targets', 'original_date',
                                                   'num_revision', 'last_revision', 'num_releases'])
    Y = pd.DataFrame.from_records(Y_list, columns = ['lifespan'])

    print(X.shape, Y.shape)
    X = X.values
    Y = Y.values

    X = clean_data(X)
    X = np.array(X)
    Y = Y.astype('float64')

    X_train, X_test, Y_train, Y_test = split_train_test(X, Y)
    model = regression_model_fit(X_train, Y_train)
    avg_value = np.average(Y_train)

    Y_predict = regression_model_predict(X_test, model)

    Y_average = np.full(Y_predict.shape, avg_value)

    regression_error = get_error(Y_predict, Y_test)
    random_error = get_error(Y_average, Y_test)
    print("Error by regression: ", regression_error)
    print("Error by average: ", random_error)
    plot(X_test[:, 0], Y_test, Y_predict, "snapshot count", "Lifespan", "Predict Lifespan")

    plot(X_test[:, 1], Y_test, Y_predict, "total targets", "Lifespan", "Predict Lifespan" )
    plot(X_test[:, 2], Y_test, Y_predict, "original date", "Lifespan", "Predict Lifespan")
    plot(X_test[:, 3], Y_test, Y_predict, "revision count", "Lifespan", "Predict Lifespan")
    plot(X_test[:, 4], Y_test, Y_predict, "last revision", "Lifespan", "Predict Lifespan")
    plot(X_test[:, 5], Y_test, Y_predict, "releases count", "Lifespan", "Predict Lifespan")



