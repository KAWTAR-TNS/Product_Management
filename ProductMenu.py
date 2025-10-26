from Controllers.ProductCRUD import *


# Function to display the main menu
def mainMenu():
    print("1. Create Product")
    print("2. Retrieve Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Get Product by ID")
    print("6. Total Products")
    print("7. Most Expensive Product")
    print("8. Least Expensive Product")
    print("9. Most Common Brand")
    print("10. Least Common Brand")
    print("11. Oldest Product")
    print("12. Newest Product")
    print("13. Product with Highest Quantity")
    print("14. Product with Lowest Quantity")
    print("15. Search Product by Name")
    print("16. Search Product by Brand")
    print("17. Exit")


# Function to execute user's choice
def executeChoice(choice):
    if choice == 1:
        print("Create Product !!!")
        name = input("Enter product name: ")
        brand = input("Enter product brand: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        createProduct(Product(name=name, brand=brand, price=price, quantity=quantity))
    elif choice == 2:
        print("Retrieving products...")
        products = getProducts()
        if products:
            for product in products:
                print(product)
        else:
            print("No products found.")
    elif choice == 3:
        print("Update Product !!!")
        productID = int(input("Enter product ID to update: "))
        name = input("Enter new product name (leave blank to skip): ")
        brand = input("Enter new product brand (leave blank to skip): ")
        price = input("Enter new product price (leave blank to skip): ")
        quantity = input("Enter new product quantity (leave blank to skip): ")
        updateProduct(productID=productID, name=name, brand=brand, price=price, quantity=quantity)
    elif choice == 4:
        productId = int(input("Enter product ID to delete: "))
        deleteProduct(productId)
    elif choice == 5:
        print("Retrieving one product...")
        productId = int(input("Enter product ID to retrieve : "))
        product = getProduct(productId)
        if product:
            print(product)
        else:
            print("Product not found")
    elif choice == 6:
        print("Total number of products:", totalProducts())
    elif choice == 7:
        result = mostExpensive()
        if result:
            print("Most Expensive Product:", result)
    elif choice == 8:
        result = leastExpensive()
        if result:
            print("Least Expensive Product:", result)
    elif choice == 9:
        result = mostCommonBrand()
        if result:
            print("Most Common Brand:", result)
    elif choice == 10:
        result = leasCommonBrand()
        if result:
            print("Least Common Brand:", result)
    elif choice == 11:
        result = oldestProduct()
        if result:
            print("Oldest Product:", result)
    elif choice == 12:
        result = newestProduct()
        if result:
            print("Newest Product:", result)
    elif choice == 13:
        result = highestQuantity()
        if result:
            print("Product with Highest Quantity:", result)
    elif choice == 14:
        result = lowestQuantity()
        if result:
            print("Product with Lowest Quantity:", result)
    elif choice == 15:
        name = input("Enter product name to search: ")
        print("Search result:", searchProductByName(name))
    elif choice == 16:
        brand = input("Enter product brand to search: ")
        print("Search result:", searchProductByBrand(brand))
    elif choice == 17:
        print("Exiting...")
        return False  # Return False to exit the loop
    else:
        print("Invalid choice.")
    return True  # Return True to continue the loop


# Main function to run the program
def main():
    while True:
        mainMenu()
        choice = int(input("Enter your choice: "))
        if not executeChoice(choice):
            break  # Exit loop if executeChoice returns False


# Run the main function
if __name__ == "__main__":
    main()
