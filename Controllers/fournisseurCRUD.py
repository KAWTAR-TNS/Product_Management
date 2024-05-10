from Modules.Fournisseur import *


# region createFournisseur
def createFournisseur(fournisseur):
    try:
        cursor.execute("""INSERT INTO Fournisseurs (firstName, lastName, tele, email, city, country)
                        VALUES (?, ?, ?, ?, ?, ?)""",
                       (fournisseur.firstName, fournisseur.lastName, fournisseur.tele, fournisseur.email,
                        fournisseur.city, fournisseur.country))
        conn.commit()
        print("Fournisseur ajouté avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de l'ajout du fournisseur:", e)


# endregion

# region getFournisseurs
def getFournisseurs() -> list[Fournisseur] | None:
    try:
        cursor.execute("SELECT * FROM Fournisseurs")
        fournisseursList = []
        fournisseurs = cursor.fetchall()
        if fournisseurs:
            for fournisseur in fournisseurs:
                fournisseursList.append(
                    Fournisseur(ID=fournisseur[0], firstName=fournisseur[1], lastName=fournisseur[2],
                                tele=fournisseur[3], email=fournisseur[4], city=fournisseur[5], country=fournisseur[6]))
            return fournisseursList
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération des fournisseurs:", e)


# endregion

# region updateFournisseur
def updateFournisseur(ID: int = 0, firstName: str = None,
                      lastName: str = None, tele: str = None,
                      email: str = None, city: str = None,
                      country: str = None):
    try:
        sql = "UPDATE Fournisseurs SET "
        parameters = []
        if firstName:
            sql += "firstName = ?, "
            parameters.append(firstName)
        if lastName:
            sql += "lastName = ?, "
            parameters.append(lastName)
        if tele:
            sql += "tele = ?, "
            parameters.append(tele)
        if email:
            sql += "email = ?, "
            parameters.append(email)
        if city:
            sql += "city = ?, "
            parameters.append(city)
        if country:
            sql += "country = ?, "
            parameters.append(country)
        sql = sql[:-2]
        sql += " WHERE ID = ?"
        parameters.append(ID)

        if cursor.execute(sql, tuple(parameters)):
            conn.commit()
            print("Fournisseur mis à jour avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour du fournisseur:", e)
# endregion

# region deleteFournisseur
def deleteFournisseur(ID):
    try:
        cursor.execute("DELETE FROM Fournisseurs WHERE ID=?", (ID,))
        conn.commit()
        print("Fournisseur supprimé avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la suppression du fournisseur:", e)
# endregion