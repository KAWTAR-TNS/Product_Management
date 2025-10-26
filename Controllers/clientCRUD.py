from Modules.Client import *


# region createClient
def createClient(client):
    try:
        cursor.execute("""INSERT INTO Clients (firstName, lastName, address, email, tele)
                        VALUES (?, ?, ?, ?, ?)""",
                       (client.firstName, client.lastName, client.address, client.email, client.tele))
        conn.commit()
        print("Client ajouté avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de l'ajout du client:", e)


# endregion

# region getClients
def getClients() -> list[Client] | None:
    try:
        cursor.execute("SELECT * FROM Clients")
        clientsList = []
        clients = cursor.fetchall()
        if clients:
            for client in clients:
                clientsList.append(
                    Client(ID=client[0], firstName=client[1], lastName=client[2],
                           address=client[3], email=client[4], tele=client[5]))
            return clientsList
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération des clients:", e)


# endregion

# region updateClient
def updateClient(ID: int = 0, firstName: str = None,
                 lastName: str = None, address: str = None,
                 email: str = None, tele: str = None):
    try:
        sql = "UPDATE Clients SET "
        parameters = []
        if firstName:
            sql += "firstName = ?, "
            parameters.append(firstName)
        if lastName:
            sql += "lastName = ?, "
            parameters.append(lastName)
        if address:
            sql += "address = ?, "
            parameters.append(address)
        if email:
            sql += "email = ?, "
            parameters.append(email)
        if tele:
            sql += "tele = ?, "
            parameters.append(tele)
        sql = sql[:-2]
        sql += " WHERE ID = ?"
        parameters.append(ID)

        if cursor.execute(sql, tuple(parameters)):
            conn.commit()
            print("Client mis à jour avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour du client:", e)


# endregion

# region deleteClient
def deleteClient(ID):
    try:
        cursor.execute("DELETE FROM Clients WHERE ID=?", (ID,))
        conn.commit()
        print("Client supprimé avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la suppression du client:", e)


# endregion

# region getClient
def getClient(ID: int) -> Client | None:
    try:
        cursor.execute("SELECT * FROM Clients WHERE ID=?", (ID,))
        client = cursor.fetchone()
        if client:
            return Client(ID=client[0], firstName=client[1], lastName=client[2],
                          address=client[3], email=client[4], tele=client[5])
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération du client:", e)
# endregion

