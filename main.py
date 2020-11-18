from config import config
from connect_database import connect_and_fetch_data
from get_stats import get_stats


if __name__ == '__main__':
    # read connection parameters
    params = config()

    # query for the database
    query = "SELECT * from final_table3"

    # fetch data from database
    database_entries = connect_and_fetch_data(query, params)

    # get statistics
    get_stats(database_entries)


