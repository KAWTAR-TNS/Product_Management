from Modules.ConnectToDB import *
from Modules.Client import *
from Controllers.clientCRUD import *


class Commande:
    def __init__(self, ID: int = 0,
                 client: Client = None,
                 dateCommande: str = ""):
        self.__ID: int = ID
        self.__client: int = client.ID
        self.__dateCommande: str = dateCommande

    # region getters
    @property
    def ID(self):
        return self.__ID

    @property
    def client(self):
        return self.__client

    @property
    def dateCommande(self):
        return self.__dateCommande

    # endregion

    # region setters
    @client.setter
    def client(self, client: Client):
        self.__client = client.ID

    @dateCommande.setter
    def dateCommande(self, value):
        self.__dateCommande = value

    # endregion

    def __str__(self):
        return f"Commande(ID={self.ID} || clientID={getClient(self.client)} || dateCommande={self.dateCommande})"

    # region createCommandeTable
    @staticmethod
    def createCommandeTable():
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS Commandes
                             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             clientID INTEGER,
                             dateCommande VARCHAR(255),
                             FOREIGN KEY (clientID) REFERENCES Clients(ID) ON DELETE CASCADE)""")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erreur lors de la création de la table 'Commandes': {e}")
    # endregion


Commande.createCommandeTable()
