import connection


def add_money():
    username = 5
    db = connection.Connection().get_connection()
    # entered_amount = int(self.amount_entry.get())

    cursor = db.cursor()
    query = "SELECT balance FROM acc_details WHERE accno = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    print(result)


add_money()
