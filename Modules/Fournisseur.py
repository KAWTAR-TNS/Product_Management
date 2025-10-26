from Modules.ConnectToDB import *
import sqlite3


class Fournisseur:
    def __init__(self, ID: int = 0,
                 firstName: str = "",
                 lastName: str = "",
                 tele: str = "",
                 email: str = "",
                 city: str = "",
                 country: str = ""):
        self.__ID: int = ID
        self.__firstName: str = firstName
        self.__lastName: str = lastName
        self.__tele: str = tele
        self.__email: str = email
        self.__city: str = city
        self.__country: str = country

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
    def tele(self):
        return self.__tele

    @property
    def email(self):
        return self.__email

    @property
    def city(self):
        return self.__city

    @property
    def country(self):
        return self.__country

    # endregion

    # region setters!!!
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName: str = firstName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName: str = lastName

    @tele.setter
    def tele(self, tele: str):
        self.__tele: str = tele

    @email.setter
    def email(self, email: str):
        self.__email: str = email

    @city.setter
    def city(self, city: str):
        self.__city: str = city

    @country.setter
    def country(self, country: str):
        self.__country: str = country

    # endregion
    def __str__(self):
        return f"ID: {self.ID}, firstName: {self.firstName}, Prénom: {self.lastName}, Téléphone: {self.tele}, Email: {self.email}, city: {self.city}, country: {self.country}"

    # region createFournisseurTable
    @staticmethod
    def createFournisseurTable():
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS Fournisseurs (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            firstName VARCHAR(255),
                            lastName VARCHAR(255),
                            tele VARCHAR(10),
                            email VARCHAR(255),
                            city VARCHAR(20),
                            country VARCHAR(20)
                            )"""
                           )
            conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)
    # endregion


Fournisseur.createFournisseurTable()
