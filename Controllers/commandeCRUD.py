from Modules.Commande import *
from Controllers.clientCRUD import *


# region createCommande
def createCommande(commande):
    try:
        cursor.execute("""INSERT INTO Commandes (clientID, dateCommande)
                          VALUES (?, ?)""",
                       (commande.client, commande.dateCommande))
        conn.commit()
        print("Commande ajoutée avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de l'ajout de la commande:", e)


# endregion

# region getCommandes
def getCommandes() -> list[Commande] | None:
    try:
        cursor.execute("SELECT * FROM Commandes")
        commandesList = []
        commandes = cursor.fetchall()
        if commandes:
            for commande in commandes:
                commandesList.append(
                    Commande(ID=commande[0], client=getClient(commande[1]), dateCommande=commande[2]))
            return commandesList
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération des commandes:", e)


# endregion

# region updateCommande
def updateCommande(ID: int = 0, client: Client = None, dateCommande: str = None):
    try:
        sql = "UPDATE Commandes SET "
        parameters = []
        if client is not None:
            sql += "clientID = ?, "
            parameters.append(client.ID)
        if dateCommande is not None:
            sql += "dateCommande = ?, "
            parameters.append(dateCommande)
        sql = sql[:-2]
        sql += " WHERE ID = ?"
        parameters.append(ID)

        cursor.execute(sql, tuple(parameters))
        conn.commit()
        print("Commande mise à jour avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour de la commande:", e)


# endregion

# region deleteCommande
def deleteCommande(ID):
    try:
        cursor.execute("DELETE FROM Commandes WHERE ID=?", (ID,))
        conn.commit()
        print("Commande supprimée avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la suppression de la commande:", e)


# endregion

# region getCommande
def getCommande(ID: int) -> Commande | None:
    try:
        cursor.execute("SELECT * FROM Commandes WHERE ID=?", (ID,))
        commande = cursor.fetchone()
        if commande:
            return Commande(ID=commande[0], client=getClient(commande[1]), dateCommande=commande[2])
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération de la commande:", e)
# endregion
