import sqlite3


def get_result(query):
    """

    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = []

        for i in connection.execute(query).fetchall():
            s = dict(i)

            result.append(s)
        return result

def get_one_query(query):
    """

    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(query).fetchone()

        return result