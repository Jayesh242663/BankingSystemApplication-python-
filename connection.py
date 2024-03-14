import mysql.connector

class Connection:
    def __init__(self):
        global username,password,host,port,database
        self.username = "root"
        self.password = "9321985498"
        self.host = "localhost"
        self.port = "3306"
        self.database = "Bankingsys"

        try:
            self.connection = mysql.connector.connect(
                user=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("CONNECTION SUCCESSFUL ;)")

        except mysql.connector.Error as e:
            print("CONNECTION FAILED :/", e)

if __name__ == "__main__":
    connection = Connection()
