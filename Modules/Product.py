from ConnectionToDB import *


class Product:
    def __init__(self, ID: int = 0,
                 name: str = "",
                 brand: str = "",
                 price: float = "",
                 quantity: int = ""):
        self.__ID = ID
        self.__name = name
        self.__brand = brand
        self.__price = price
        self.__quantity = quantity

    # region getters!!!
    @property
    def ID(self):
        return self.__ID

    @property
    def name(self):
        return self.__name

    @property
    def brand(self):
        return self.__brand

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    # endregion

    # region setters!!!
    @name.setter
    def name(self, productName: str):
        self.__name = productName

    @brand.setter
    def brand(self, productBrand: str):
        self.__brand = productBrand

    @price.setter
    def price(self, productPrice: str):
        self.__price = productPrice

    @quantity.setter
    def quantity(self, productQuantity: str):
        self.__quantity = productQuantity

    # endregion

    def __str__(self):
        return f"ID: {self.ID}, Name: {self.name}, Brand: {self.brand}, Price: {self.price}, Quantity: {self.quantity}"

    @staticmethod
    def createProductTable():
        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS products (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255),
                    brand VARCHAR(255),
                    price REAL,
                    quantity INTEGER)""")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erreur lors de la création de la table 'Product': {e}")


Product.createProductTable()
