from Modules.ConnectToDB import *
from Controllers.commandeCRUD import *
from Controllers.ProductCRUD import *


class LigneCommande:
    def __init__(self, ligneID: int = 0,
                 commande: Commande = None,
                 product: Product = None,
                 quantiteCommande: int = 0):
        self.__ligneID = ligneID
        self.__commande = commande.ID
        self.__product = product.ID
        self.__quantiteCommande = quantiteCommande

    @property
    def ligneID(self):
        return self.__ligneID

    @property
    def commande(self):
        return self.__commande

    @property
    def product(self):
        return self.__product

    @property
    def quantiteCommande(self):
        return self.__quantiteCommande

    @commande.setter
    def commande(self, commande: Commande):
        self.__commande = commande.ID

    @product.setter
    def product(self, product: Product):
        self.__product = product.ID

    @quantiteCommande.setter
    def quantiteCommande(self, quantiteCommande: int):
        self.__quantiteCommande = quantiteCommande

    def __str__(self):
        return f"LigneCommande(ligneID={self.ligneID}, commande={getCommande(self.commande)}, article={getProduct(self.product)}, quantiteCommande={self.quantiteCommande})"

    @staticmethod
    def createLigneCommandeTable():
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS LigneCommandes
                             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             commandeID INTEGER,
                             productID INTEGER,
                             quantiteCommande INTEGER,
                             FOREIGN KEY (commandeID) REFERENCES Commandes(ID) ON DELETE CASCADE,
                             FOREIGN KEY (articleID) REFERENCES Articles(ID) ON DELETE CASCADE)""")
            conn.commit()
            print("Table 'LigneCommandes' créée avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la création de la table 'LigneCommandes': {e}")
