from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    """
    This function is used to pick the configuration from the section
    in the provided file

    :param filename: The path of the file which contains the configurations
    :param section: The section inside the file which contains the configuration needed to connect to the database
    :return: the database config needed to connect

    """
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
