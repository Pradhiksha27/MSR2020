from config import config
from connect_database import connect_and_fetch_data
from get_stats import get_stats
import pandas as pd


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



