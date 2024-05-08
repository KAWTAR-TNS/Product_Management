from ConnectionToDB import *


class Product:
    def __init__(self, name: str, brand: str, price: float, quantity: int, addedDate: str, ID: int = 0):
        self.__ID = ID
        self.__name = name
        self.__brand = brand
        self.__price = price
        self.__quantity = quantity
        self.__addedDate = addedDate

    @property
    def ID(self):
        return self.__ID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, productName: str):
        self.__name = productName

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, productBrand: str):
        self.__brand = productBrand

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, productPrice: str):
        self.__price = productPrice

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, productQuantity: str):
        self.__quantity = productQuantity

    @property
    def addedDate(self):
        return self.__addedDate

    @addedDate.setter
    def addedDate(self, productAddedDate: str):
        self.__addedDate = productAddedDate

    def __str__(self):
        return f"Name: {self.name}, Brand: {self.brand}, Price: {self.price}, Quantity: {self.quantity}, Date Added: {self.addedDate}"

    @staticmethod
    def createProductTable():
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                brand VARCHAR(255) NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                addedDate TEXT NOT NULL
            );
            """
        )
        conn.commit()


Product.createProductTable()
