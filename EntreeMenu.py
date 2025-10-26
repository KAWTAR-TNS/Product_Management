from Controllers.EntreeCRUD import *
from Controllers.ProductCRUD import *
from Controllers.fournisseurCRUD import *


# Main menu function
def mainMenu():
    print("1. Create Entree")
    print("2. Retrieve Entrees")
    print("3. Update Entree")
    print("4. Delete Entree")
    print("5. Get Entree by ID")
    print("6. Exit")


# Function to execute user's choice
def executeChoice(choice):
    if choice == 1:
        print("Create Entree !!!")
        createNewFournisseur = input("Do you have a new fournisseur for this entree? (y/n): ").lower()
        if createNewFournisseur == "y":
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
        elif createNewFournisseur == "n":
            pass
        else:
            print("Invalid choice. Please try again.")

        createNewProduct = input("Do you have a new Product for this entree? (y/n): ").lower()
        if createNewProduct == "y":
            # Add a new product
            name = input("Enter product name: ")
            brand = input("Enter product brand: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            createProduct(Product(name=name, brand=brand, price=price, quantity=quantity))
        elif createNewProduct == "n":
            pass
        else:
            print("Invalid choice. Please try again.")

        # Proceed to add a new entree
        print("Your fournisseurs :")
        for fournisseur in getFournisseurs():
            print(fournisseur)
        fournisseurID = int(input("Enter fournisseur ID: "))
        fournisseur = getFournisseur(fournisseurID)
        if not fournisseur:
            print("Fournisseur not found.")
            return

        print("Your products :")
        for product in getProducts():
            print(product)
        productID = int(input("Enter product ID: "))
        product = getProduct(productID)
        if not product:
            print("Product not found.")
            return

        quantity = int(input("Enter quantity: "))
        createEntree(Entree(fournisseur=fournisseur, product=product, quantity=quantity))
    elif choice == 2:
        print("Retrieving entrees...")
        entrees = getEntrees()
        if entrees:
            for entree in entrees:
                print(entree)
        else:
            print("No entrees found.")
    elif choice == 3:
        print("Update Entree !!!")
        ID = int(input("Enter entree ID to update: "))
        fournisseurIdInput = input("Enter fournisseur ID (leave blank to skip): ")
        if fournisseurIdInput.strip():
            fournisseur = getFournisseur(int(fournisseurIdInput))
        else:
            fournisseur = None
        product_id_input = input("Enter product ID (leave blank to skip): ")
        if product_id_input.strip():
            product = getProduct(int(product_id_input))
        else:
            product = None

        quantity = int(input("Enter new quantity (leave blank to skip): "))
        updateEntree(ID=ID, fournisseur=fournisseur, product=product, quantity=quantity)
    elif choice == 4:
        ID = int(input("Enter entree ID to delete: "))
        deleteEntree(ID)
    elif choice == 5:
        print("Retrieving one entree...")
        ID = int(input("Enter entree ID to retrieve : "))
        entree = getEntree(ID)
        if entree:
            print(entree)
        else:
            print("Entree not found")
    elif choice == 6:
        print("Exiting...")
    else:
        print("Invalid choice.")


# Main function to run the program
def main():
    while True:
        mainMenu()
        choice = int(input("Enter your choice: "))
        if choice == 6:
            break
        executeChoice(choice)


if __name__ == "__main__":
    main()
