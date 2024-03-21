import mysql.connector

class Connection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.cnx = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                port='3306',
                database='bankingsys'
            )
        return cls._instance

    def get_connection(self):
        return self.cnx

    # def __init__(self):
    #     global username,password,host,port,database
    #     self.username = "root"
    #     self.password = "9321985498"
    #     self.host = "localhost"
    #     self.port = "3306"
    #     self.database = "Bankingsys"
    #
    #     try:
    #         self.connection = mysql.connector.connect(
    #             user=self.username,
    #             password=self.password,
    #             host=self.host,
    #             port=self.port,
    #             database=self.database
    #         )
    #         self.cursor = self.connection.cursor()
    #         print("CONNECTION SUCCESSFUL ;)")
    #         return self.cursor
    #
    #     except mysql.connector.Error as e:
    #         print("CONNECTION FAILED :/", e)

if __name__ == "__main__":
    connection = Connection()
