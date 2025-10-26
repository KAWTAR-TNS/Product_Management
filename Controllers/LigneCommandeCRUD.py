from Modules.LigneCommande import *


# region Create ligne commande
def createLigneCommande(ligneCommande: LigneCommande):
    try:
        cursor.execute("""
            INSERT INTO LigneCommandes (commandeID, productID, quantiteCommande)
            VALUES (?, ?, ?)""",
                       (ligneCommande.commande, ligneCommande.product.ID, ligneCommande.quantiteCommande))
        conn.commit()
        print("Ligne de commande ajoutée avec succès.")
        decreaseProductQuantity(ligneCommande.product.ID, ligneCommande.quantiteCommande)
    except sqlite3.Error as e:
        print("Erreur lors de l'ajout de la ligne de commande :", e)


# endregion

# region Retrieve ligne commandes
def getLigneCommandes() -> list[LigneCommande] | None:
    try:
        cursor.execute("SELECT * FROM LigneCommandes")
        lignesCommandesList = []
        lignesCommandes = cursor.fetchall()
        if lignesCommandes:
            for ligneCommande in lignesCommandes:
                lignesCommandesList.append(LigneCommande(ligneID=ligneCommande[0],
                                                         commande=getCommande(ligneCommande[1]),
                                                         product=getProduct(ligneCommande[2]),
                                                         quantiteCommande=ligneCommande[3]))
            return lignesCommandesList
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération des lignes de commande :", e)


# endregion

# region Update ligne commande
def updateLigneCommande(ID: int = 0, commande: Commande = None, product: Product = None, quantiteCommande: int = 0):
    try:
        sql = "UPDATE LigneCommandes SET "
        parameters = []
        if commande:
            sql += "commandeID = ?, "
            parameters.append(commande.ID)
        if product:
            sql += "articleID = ?, "
            parameters.append(product.ID)
        if quantiteCommande:
            sql += "quantiteCommande = ?, "
            parameters.append(quantiteCommande)
        sql = sql[:-2]
        sql += " WHERE ID = ?"
        parameters.append(ID)

        cursor.execute(sql, tuple(parameters))
        conn.commit()
        print("Ligne de commande mise à jour avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour de la ligne de commande :", e)


# endregion

# region Delete ligne commande
def deleteLigneCommande(ID):
    try:
        cursor.execute("DELETE FROM LigneCommandes WHERE ID=?", (ID,))
        conn.commit()
        print("Ligne de commande supprimée avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de la suppression de la ligne de commande :", e)


# endregion

# region Get ligne commande by ID
def getLigneCommande(ID: int) -> LigneCommande | None:
    try:
        cursor.execute("SELECT * FROM LigneCommandes WHERE ID=?", (ID,))
        ligneCommande = cursor.fetchone()
        if ligneCommande:
            return LigneCommande(ligneID=ligneCommande[0],
                                 commande=getCommande(ligneCommande[1]),
                                 product=getProduct(ligneCommande[2]),
                                 quantiteCommande=ligneCommande[3])
        else:
            return None
    except sqlite3.Error as e:
        print("Erreur lors de la récupération de la ligne de commande :", e)

# endregion
