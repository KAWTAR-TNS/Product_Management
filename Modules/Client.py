from Modules.ConnectToDB import *


class Client:
    def __init__(self, ID: int = 0,
                 firstName: str = "",
                 lastName: str = "",
                 address: str = "",
                 email: str = "",
                 tele: str = ""):
        self.__ID: int = ID
        self.__firstName: str = firstName
        self.__lastName: str = lastName
        self.__address: str = address
        self.__email: str = email
        self.__tele: str = tele

    # region getters!!!
    @property
    def ID(self):
        return self.__ID

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def address(self):
        return self.__address

    @property
    def email(self):
        return self.__email

    @property
    def tele(self):
        return self.__tele

    # endregion

    # region setters!!!
    @firstName.setter
    def firstName(self, value):
        self.__firstName = value

    @lastName.setter
    def lastName(self, value):
        self.__lastName = value

    @address.setter
    def address(self, value):
        self.__address = value

    @email.setter
    def email(self, value):
        self.__email = value

    @tele.setter
    def tele(self, value):
        self.__tele = value

    # endregion

    def __str__(self):
        return f"User(ID={self.ID}, firstName={self.firstName}, lastName={self.lastName}, address={self.address}, email={self.email}, tele={self.tele})"

    @staticmethod
    def createClientTable():
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS Clients
                             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             firstName VARCHAR(255),
                             lastName VARCHAR(255),
                             address VARCHAR(255),
                             email VARCHAR(255),
                             tele VARCHAR(255))""")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


Client.createClientTable()
