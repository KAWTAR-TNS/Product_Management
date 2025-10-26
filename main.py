from Controllers.ProductCRUD import *
from ProductMenu import leastCommonBrand


def main():
    print("Welcome to Product Management System")
    print("1. Create a product")
    print("2. Update a product")
    print("3. Delete a product")
    print("4. Retrieve all products")
    print("5. Get total number of products")
    print("6. Get most expensive product")
    print("7. Get least expensive product")
    print("8. Get most common brand")
    print("9. Get least common brand")
    print("10. Get oldest product")
    print("11. Get newest product")
    print("12. Get product with highest quantity")
    print("13. Get product with lowest quantity")
    print("14. Search product by name")
    print("15. Search product by brand")
    print("0. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter product name: ")
            brand = input("Enter product brand: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            createProduct(Product(name=name, brand=brand, price=price, quantity=quantity))
        elif choice == '2':
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name (leave blank to skip): ")
            brand = input("Enter new product brand (leave blank to skip): ")
            price = input("Enter new product price (leave blank to skip): ")
            quantity = input("Enter new product quantity (leave blank to skip): ")
            added_date = input("Enter new product added date (YYYY-MM-DD) (leave blank to skip): ")
            updateProduct(productId=product_id, name=name, brand=brand, price=price, quantity=quantity,
                          addedDate=added_date)
        elif choice == '3':
            product_id = int(input("Enter product ID to delete: "))
            deleteProduct(product_id)
        elif choice == '4':
            products = getProducts()
            if products:
                for product in products:
                    print(product)
            else:
                print("No products found.")
        elif choice == '5':
            print("Total products:", totalProducts())
        elif choice == '6':
            print("Most expensive product:", mostExpensive())
        elif choice == '7':
            print("Least expensive product:", leastExpensive())
        elif choice == '8':
            print("Most common brand:", mostCommonBrand())
        elif choice == '9':
            print("Least common brand:", leastCommonBrand())
        elif choice == '10':
            print("Oldest product:", oldestProduct())
        elif choice == '11':
            print("Newest product:", newestProduct())
        elif choice == '12':
            print("Product with highest quantity:", highestQuantity())
        elif choice == '13':
            print("Product with lowest quantity:", lowestQuantity())
        elif choice == '14':
            name = input("Enter product name to search: ")
            print("Search result:", searchProductByName(name))
        elif choice == '15':
            brand = input("Enter product brand to search: ")
            print("Search result:", searchProductByBrand(brand))
        elif choice == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 15.")


if __name__ == "__main__":
    main()
