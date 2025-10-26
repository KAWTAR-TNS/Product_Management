from Controllers.clientCRUD import *
from Controllers.commandeCRUD import *
from Controllers.fournisseurCRUD import *
from Controllers.EntreeCRUD import *


def main_menu():
    print("Welcome to the inventory management system!")
    print("1. Manage entrees")
    print("2. Manage sortie")
    print("3. Check stock")
    print("4. Exit")
    choice = input("Please enter your choice: ")
    return choice


def manage_entrees_menu():
    print("Manage Entrees Menu:")
    print("1. Add a new fournisseur")
    print("2. Add a new entree")
    print("3. View all entrees")
    print("4. Back to main menu")
    choice = input("Please enter your choice: ")
    return choice


def manage_sortie_menu():
    print("Manage Sortie Menu:")
    print("1. Create a new commande")
    print("2. Add a new client")
    print("3. View all commandes")
    print("4. Back to main menu")
    choice = input("Please enter your choice: ")
    return choice


def check_stock_menu():
    print("Check Stock Menu:")
    print("1. View stock quantities")
    print("2. View product details")
    print("3. Back to main menu")
    choice = input("Please enter your choice: ")
    return choice


# Your menu functions go here

while True:
    choice = main_menu()

    if choice == "1":
        while True:
            entrees_choice = manage_entrees_menu()
            if entrees_choice == "1":
                # Add a new fournisseur
                firstName = input("Enter first name: ")
                lastName = input("Enter last name: ")
                tele = input("Enter telephone number: ")
                email = input("Enter email address: ")
                city = input("Enter city: ")
                country = input("Enter country: ")
                fournisseur = Fournisseur(firstName=firstName, lastName=lastName, tele=tele,
                                          email=email, city=city, country=country)
                createFournisseur(fournisseur)
            elif entrees_choice == "2":
                create_new_fournisseur = input("Do you have a new fournisseur for this entree? (y/n): ").lower()
                if create_new_fournisseur == "y":
                    # Add a new fournisseur
                    firstName = input("Enter first name: ")
                    lastName = input("Enter last name: ")
                    tele = input("Enter telephone number: ")
                    email = input("Enter email address: ")
                    city = input("Enter city: ")
                    country = input("Enter country: ")
                    fournisseur = Fournisseur(firstName=firstName, lastName=lastName, tele=tele,
                                              email=email, city=city, country=country)
                    createFournisseur(fournisseur)
                elif create_new_fournisseur == "n":
                    pass
                else:
                    print("Invalid choice. Please try again.")

                # Proceed to add a new entree
                entree = Entree()
                entree.fournisseur = getFournisseur(int(input("Enter fournisseur ID: ")))
                entree.product = getProduct(int(input("Enter product ID: ")))
                entree.quantity = int(input("Enter quantity: "))
                createEntree(entree)

            elif entrees_choice == "3":
                # View all entrees
                entrees = getEntrees()
                if entrees:
                    for entree in entrees:
                        print(entree)
                else:
                    print("No entrees found.")
            elif entrees_choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        while True:
            sortie_choice = manage_sortie_menu()
            if sortie_choice == "1":
                # Create a new commande
                client_id = getClient(int(input("Enter client ID: ")))
                date_commande = input("Enter date of the commande (YYYY-MM-DD HH:MM:SS): ")
                commande = Commande(client=client_id, dateCommande=date_commande)
                createCommande(commande)
            elif sortie_choice == "2":
                # Add a new client
                first_name = input("Enter client's first name: ")
                last_name = input("Enter client's last name: ")
                address = input("Enter client's address: ")
                email = input("Enter client's email: ")
                tele = input("Enter client's phone number: ")
                client = Client(firstName=first_name, lastName=last_name, address=address, email=email, tele=tele)
                createClient(client)
            elif sortie_choice == "3":
                # View all commandes
                commandes = getCommandes()
                if commandes:
                    for commande in commandes:
                        print(commande)
                else:
                    print("No commandes found.")
            elif sortie_choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":
        while True:
            stock_choice = check_stock_menu()
            if stock_choice == "1":
                # View stock quantities
                products = getProducts()
                if products:
                    for product in products:
                        print(f"{product.name}: {product.quantity}")
                else:
                    print("No products found.")
            elif stock_choice == "2":
                # View product details
                products = getProducts()
                if products:
                    for product in products:
                        print(product)
                else:
                    print("No products found.")
            elif stock_choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
