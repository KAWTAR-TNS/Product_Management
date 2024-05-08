from Controllers.ProductCRUD import *


def main():
    while True:
        print("\nStock Management System Menu:")
        print("1. Add a new product")
        print("2. Update product")
        print("3. Delete product")
        print("4. Retrieve products")
        print("5. Total products")
        print("6. Most expensive product")
        print("7. Least expensive product")
        print("8. Most common brand")
        print("9. Least common brand")
        print("10. Oldest product")
        print("11. Newest product")
        print("12. Product with highest quantity")
        print("13. Product with lowest quantity")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name : ")
            brand = input("Enter product brand : ")
            price = float(input("Enter product price : "))
            quantity = int(input("Enter product quantity : "))
            addedDate = input("Enter product addition date (YYYY-MM-DD) : ")
            createProduct(Product(name=name, brand=brand, price=price, quantity=quantity, addedDate=addedDate))
        elif choice == "2":
            print("Update product : ", updateProduct())
        elif choice == "3":
            productID = input("Enter product ID : ")
            print("Delete product : ", deleteProduct(productID))
        elif choice == "4":
            for product in getProducts():
                print(product)
        elif choice == "5":
            print("Total products : ", totalProducts())
        elif choice == "6":
            print("Most expensive product : ", mostExpensive())
        elif choice == "7":
            print("Least expensive product : ", leastExpensive())
        elif choice == "8":
            print("Most common brand : ", mostCommonBrand())
        elif choice == "9":
            print("Least common brand : ", leasCommonBrand())
        elif choice == "10":
            print("Oldest product : ", oldestProduct())
        elif choice == "11":
            print("Newest product : ", newestProduct())
        elif choice == "12":
            print("Product with highest quantity : ", highestQuantity())
        elif choice == "13":
            print("Product with lowest quantity : ", lowestQuantity())
        elif choice == "14":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 14.")
    conn.close()


if __name__ == "__main__":
    main()
