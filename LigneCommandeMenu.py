from Controllers.LigneCommandeCRUD import *


# Main menu function
def mainMenu():
    print("1. Create Ligne Commande")
    print("2. Retrieve Ligne Commandes")
    print("3. Update Ligne Commande")
    print("4. Delete Ligne Commande")
    print("5. Get Ligne Commande by ID")
    print("6. Exit")


# Function to execute user's choice
def executeChoice(choice):
    if choice == 1:
        print("Create Ligne Commande !!!")
        commandeID = int(input("Enter commande ID: "))
        commande = getCommande(commandeID)
        if not commande:
            print("Commande not found.")
            return
        productID = int(input("Enter product ID: "))
        product = getProduct(productID)
        if not product:
            print("Product not found.")
            return
        quantiteCommande = int(input("Enter quantity: "))
        createLigneCommande(LigneCommande(commande=commande, product=product, quantiteCommande=quantiteCommande))
    elif choice == 2:
        print("Retrieving ligne commandes...")
        ligneCommandes = getLigneCommandes()
        if ligneCommandes:
            for ligneCommande in ligneCommandes:
                print(ligneCommande)
        else:
            print("No ligne commandes found.")
    elif choice == 3:
        print("Update Ligne Commande !!!")
        ID = int(input("Enter ligne commande ID to update: "))
        commandeIDInput = int(input("Enter commande ID (leave blank to skip): "))
        if commandeIDInput:
            commande = getCommande(commandeIDInput)
        else:
            commande = None
        productID = int(input("Enter product ID (leave blank to skip): "))
        product = getProduct(productID) if productID else None
        quantiteCommande = int(input("Enter new quantity (leave blank to skip): "))
        updateLigneCommande(ID=ID, commande=commande, product=product, quantiteCommande=quantiteCommande)
    elif choice == 4:
        ID = int(input("Enter ligne commande ID to delete: "))
        deleteLigneCommande(ID)
    elif choice == 5:
        print("Retrieving one ligne commande...")
        ID = int(input("Enter ligne commande ID to retrieve : "))
        ligneCommande = getLigneCommande(ID)
        if ligneCommande:
            print(ligneCommande)
        else:
            print("Ligne commande not found")
    elif choice == 6:
        print("Exiting...")
    else:
        print("Invalid choice.")


# Main function to run the program
def main():
    databaseName = "your_database_name.db"  # Replace with your database name
    conn, cursor = connectToDatabase(databaseName)
    if conn and cursor:
        while True:
            mainMenu()
            choice = int(input("Enter your choice: "))
            if choice == 6:
                break
            executeChoice(choice)
        closeConnection(conn)
    else:
        print("Error connecting to database. Exiting...")


if __name__ == "__main__":
    main()
