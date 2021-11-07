import pymysql

"""
step-1 This .db_config_flink file consist of mysql database credentials.
A sample file is present in the codebase which ideally should not be present in codebase and should be kept somewhere in server.

step-2 A class having multiple methods for connecting, executing, fetching the data from mysql db.
"""

# step-1 .db_config file
with open('.db_config_flink') as in_config:
    exec(in_config.read())

# step-2 A class having multiple methods for manipulating mysql db.
class MySQLconnection():
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user
        self.password = password
        self.port = int(port)

    def __disconnect__(self):
        self.dbconn.commit()
        self.dbconn.close()

    def execute_script(self, query):
        self.__connect__()
        self.db_cursor.execute(query)
        self.__disconnect__()

    def __connect__(self):
        self.dbconn = pymysql.connections.Connection(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port
        )
        self.db_cursor = self.dbconn.cursor()

    def fetch(self, query, column_list):
        self.__connect__()
        self.db_cursor.execute(query)
        result_fetched = self.db_cursor.fetchall()
        result_list = [i for i in result_fetched]
        result_df = pd.DataFrame(result_list, columns=column_list)
        self.__disconnect__()
        return result_df


# mysql connection object
mysql_conn_obj = MySQLconnection(host=MYSQL_SRC_HOST, user=MYSQL_SRC_USER, password=MYSQL_SRC_PASSWORD, port=MYSQL_SRC_PORT)
