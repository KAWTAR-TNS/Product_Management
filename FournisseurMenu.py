from Controllers.fournisseurCRUD import *


# Main menu function
def mainMenu():
    print("1. Create Fournisseur")
    print("2. Retrieve Fournisseurs")
    print("3. Update Fournisseur")
    print("4. Delete Fournisseur")
    print("5. Get Fournisseur by ID")
    print("6. Exit")


# Function to execute user's choice
def executeChoice(choice):
    if choice == 1:
        print("Create Fournisseur !!!")
        firstName = input("Enter fournisseur first name: ")
        lastName = input("Enter fournisseur last name: ")
        tele = input("Enter fournisseur telephone: ")
        email = input("Enter fournisseur email: ")
        city = input("Enter fournisseur city: ")
        country = input("Enter fournisseur country: ")
        createFournisseur(Fournisseur(firstName=firstName, lastName=lastName, tele=tele, email=email, city=city, country=country))
    elif choice == 2:
        print("Retrieving fournisseurs...")
        fournisseurs = getFournisseurs()
        if fournisseurs:
            for fournisseur in fournisseurs:
                print(fournisseur)
        else:
            print("No fournisseurs found.")
    elif choice == 3:
        print("Update Fournisseur !!!")
        ID = int(input("Enter fournisseur ID to update: "))
        firstName = input("Enter new fournisseur first name (leave blank to skip): ")
        lastName = input("Enter new fournisseur last name (leave blank to skip): ")
        tele = input("Enter new fournisseur telephone (leave blank to skip): ")
        email = input("Enter new fournisseur email (leave blank to skip): ")
        city = input("Enter new fournisseur city (leave blank to skip): ")
        country = input("Enter new fournisseur country (leave blank to skip): ")
        updateFournisseur(ID=ID, firstName=firstName, lastName=lastName, tele=tele, email=email, city=city, country=country)
    elif choice == 4:
        ID = int(input("Enter fournisseur ID to delete: "))
        deleteFournisseur(ID)
    elif choice == 5:
        print("Retrieving one fournisseur...")
        ID = int(input("Enter fournisseur ID to retrieve : "))
        fournisseur = getFournisseur(ID)
        if fournisseur:
            print(fournisseur)
        else:
            print("Fournisseur not found")
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
