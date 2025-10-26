from Controllers.ProductCRUD import *
from Controllers.fournisseurCRUD import *
from datetime import datetime


class Entree:
    def __init__(self, entreeID: int = 0,
                 fournisseur: Fournisseur = None,
                 product: Product = None,
                 quantity: int = 0,
                 dateEntree: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.__entreeID = entreeID
        self.__fournisseur = fournisseur.ID
        self.__product = product.ID
        self.__quantity = quantity
        self.__dateEntree = dateEntree

    # region getters!!!
    @property
    def entreeID(self):
        return self.__entreeID

    @property
    def fournisseur(self):
        return self.__fournisseur

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @property
    def dateEntree(self):
        return self.__dateEntree
    # endregion

    # region setters!!!
    @fournisseur.setter
    def fournisseur(self, fournisseur: Fournisseur):
        self.__fournisseur = fournisseur.ID

    @product.setter
    def product(self, product: Product):
        self.__product = product.ID

    @quantity.setter
    def quantity(self, quantite: int):
        self.__quantity = quantite
    # endregion

    def __str__(self):
        return f"Entree(ID={self.entreeID}, Fournisseur={getFournisseur(self.fournisseur)}, Product={getProduct(self.product)}, Quantite={self.quantity}, DateEntree={self.dateEntree})"

    @staticmethod
    def createEntreeTable():
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS Entrees
                                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 fournisseurID INTEGER,
                                 productID INTEGER,
                                 quantity INTEGER,
                                 dateEntree TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                 FOREIGN KEY (fournisseurID) REFERENCES Fournisseurs(ID) ON DELETE CASCADE,
                                 FOREIGN KEY (productID) REFERENCES Products(ID) ON DELETE CASCADE)""")
            conn.commit()
            print("Table 'Entrees' créée avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la création de la table 'Entrees': {e}")


Entree.createEntreeTable()
