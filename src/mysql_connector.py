import mysql.connector
import time

class Mysql():
    def __init__(self, host, user, pw):
        max_retries = 30
        retries = 0

        while True:
            try:
                connection = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=pw
                )

                connection.close()
                print("MySQL is ready.")
                break
            except mysql.connector.Error as err:
                
                print(f"Waiting for MySQL... ({err})")
                time.sleep(1)
                retries += 1

                if retries >= max_retries:
                    print("Unable to connect to MySQL. Exiting.")
                    exit(1)
        self.mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=pw
        )

        self.mycursor = self.mydb.cursor()

    def query(self, text):
        self.mycursor.execute(text)
        try:
            self.mydb.commit()
        except Exception:
            pass
        return self.mycursor.fetchall()


#myclass = Mysql("127.0.0.1", "root", "qwerty1234")
#res = myclass.query("show databases")
#print(res)
