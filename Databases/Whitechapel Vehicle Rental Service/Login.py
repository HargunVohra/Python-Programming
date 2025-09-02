from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

class Login:
    def __init__(self, Username, Password):
        self.__Username = Username
        self.__Password = Password

    def ValidateLogin(self, cursor):
        cursor.execute(
            "SELECT * FROM SignUpDetails WHERE Username=%s AND Password=%s",
            (self.__Username, self.__Password)
        )
        Result = cursor.fetchone()
        return Result