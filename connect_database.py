import psycopg2


def connect_and_fetch_data(query, params):
    """
    This function is used to connect to the database and fetch the rows
    from the database, given the query and config params of the database.

    :param query: The select query to be used to fetch data
    :param params: The parameters used to contact the database server
    :return: list of rows in database fetched from the query
    """
    conn = None
    try:
        # connect to the PostgreSQL server
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute(query)

        # display the PostgreSQL database server version
        db_entries = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()

        return db_entries
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error occurred while trying to connect the database: ", error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")
