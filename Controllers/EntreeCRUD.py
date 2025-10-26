from Modules.Entree import *
from Controllers.ProductCRUD import *
from Controllers.fournisseurCRUD import *


# region Create entree
def createEntree(entree: Entree):
    try:
        existing_product = getProduct(entree.product)
        if existing_product:
            increaseProductQuantity(entree.product, entree.quantity)
        else:
            createProduct(entree.product)
        cursor.execute("""
            INSERT INTO Entrees (fournisseurID, productID, quantity)
            VALUES (?, ?, ?)""",
                       (entree.fournisseur, entree.product, entree.quantity))

        conn.commit()
        print("Entrée ajoutée avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de l'ajout de l'entrée :", e)


# endregion

# region Retrieve entrees
def getEntrees() -> list[Entree] | None:
    try:
        cursor.execute("SELECT * FROM Entrees")
        entrees_list = []
        entrees = cursor.fetchall()
        if entrees:
            for entree in entrees:
                entrees_list.append(Entree(entreeID=entree[0],
                                           fournisseur=getFournisseur(entree[1]),
                                           product=getProduct(entree[2]),
                                           quantity=entree[3],
                                           dateEntree=entree[4]))
            return entrees_list
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération des entrées :", e)


# endregion

# region Update entree
def updateEntree(ID: int = 0, fournisseur: Fournisseur = None, product: Product = None, quantity: int = 0):
    try:
        sql = "UPDATE Entrees SET "
        parameters = []
        if fournisseur:
            sql += "fournisseurID = ?, "
            parameters.append(fournisseur.ID)
        if product:
            sql += "productID = ?, "
            parameters.append(product.ID)
        if quantity:
            sql += "quantity = ?, "
            parameters.append(quantity)
        sql = sql[:-2]
        sql += " WHERE ID = ?"
        parameters.append(ID)

        cursor.execute(sql, tuple(parameters))
        conn.commit()
        print("Entrée mise à jour avec succès.")

        existingEntree = getEntree(ID)
        if existingEntree:
            quantityDifference = quantity - existingEntree.quantity
            if quantityDifference > 0:
                increaseProductQuantity(existingEntree.product, quantityDifference)
            elif quantityDifference < 0:
                decreaseProductQuantity(existingEntree.product, abs(quantityDifference))

    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour de l'entrée :", e)



# endregion

# region Delete entree
def deleteEntree(ID):
    try:
        cursor.execute("DELETE FROM Entrees WHERE ID=?", (ID,))
        conn.commit()
        print("Entrée supprimée avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la suppression de l'entrée :", e)


# endregion

# region Get entree by ID
def getEntree(ID: int) -> Entree | None:
    try:
        cursor.execute("SELECT * FROM Entrees WHERE ID=?", (ID,))
        entree = cursor.fetchone()
        if entree:
            return Entree(entreeID=entree[0],
                          fournisseur=getFournisseur(entree[1]),
                          product=getProduct(entree[2]),
                          quantity=entree[3],
                          dateEntree=entree[4])
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération de l'entrée :", e)

# endregion
