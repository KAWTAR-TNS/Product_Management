from Modules.Product import *


# region Create product
def createProduct(product: Product):
    try:
        cursor.execute(
            """
                INSERT INTO products (name, brand, price, quantity) VALUES (?, ?, ?, ?)
            """,
            (product.name, product.brand, product.price, product.quantity)
        )
        conn.commit()
        print("Product created successfully!!!")
    except sqlite3.Error as e:
        print("Error while creating product : ", e)


# endregion

# region Retrieve products
def getProducts() -> list[Product] | None:
    try:
        cursor.execute("SELECT * FROM Products")
        productsList = []
        products = cursor.fetchall()
        if products:
            for product in products:
                productsList.append(Product(ID=product[0], name=product[1], brand=product[2],
                                            price=product[3], quantity=product[4]))
            return productsList
        else:
            return None
    except sqlite3.Error as e:
        print("Error while retrieving products : ", e)


# endregion

# region update product
def updateProduct(productID: int = 0, name: str = None,
                  brand: str = None, price: str = None,
                  quantity: str = None):
    try:
        sql: str = "UPDATE PRODUCTS SET "
        parameters = []
        if name:
            sql += "name = ?, "
            parameters.append(name)
        if brand:
            sql += "brand = ?, "
            parameters.append(brand)
        if price:
            sql += "price = ?, "
            parameters.append(price)
        if quantity:
            sql += "quantity = ?, "
            parameters.append(quantity)
        sql = sql[:-2]
        sql += " WHERE ID = ?"
        parameters.append(productID)
        if cursor.execute(sql, tuple(parameters)):
            conn.commit()
    except sqlite3.Error as e:
        print("Error while updating product product: ", e)


# endregion

# region deleting product
def deleteProduct(productId):
    try:
        delete_product_sql = "DELETE FROM products WHERE id = ?;"
        cursor.execute(delete_product_sql, (productId,))
        conn.commit()
    except sqlite3.Error as e:
        print("Error while deleting product : ", e)


# endregion

# region Get product by ID
def getProduct(id: int) -> Product | None:
    try:
        cursor.execute("SELECT * FROM products WHERE ID=?", (id,))
        product = cursor.fetchone()
        if product:
            return Product(ID=product[0], name=product[1], brand=product[2], price=product[3], quantity=product[4])
        else:
            return None
    except sqlite3.Error as e:
        print("Error while getting product by ID:", e)


# endregion

# region increaseProductQuantity
def increaseProductQuantity(productId: int, quantityToAdd: int):
    try:
        # Retrieve the current quantity of the product
        currentQuantity = cursor.execute("SELECT quantity FROM products WHERE ID=?", (productId,)).fetchone()[0]
        # Calculate the new quantity by adding the specified quantity to the current quantity
        newQuantity = currentQuantity + quantityToAdd
        # Update the product with the new quantity
        cursor.execute("UPDATE products SET quantity=? WHERE ID=?", (newQuantity, productId))
        conn.commit()
        print("Product quantity updated successfully!!!")
    except sqlite3.Error as e:
        print("Error while updating product quantity: ", e)


# endregion

# region Decrease product quantity
def decreaseProductQuantity(productId: int, quantityToSubtract: int):
    try:
        currentQuantity = cursor.execute("SELECT quantity FROM products WHERE ID=?", (productId,)).fetchone()[0]
        if currentQuantity >= quantityToSubtract:
            newQuantity = currentQuantity - quantityToSubtract
            cursor.execute("UPDATE products SET quantity=? WHERE ID=?", (newQuantity, productId))
            conn.commit()
            print("Product quantity decreased successfully!!!")
        else:
            print("Not enough quantity available to subtract.")
    except sqlite3.Error as e:
        print("Error while updating product quantity: ", e)


# endregion


# region Total products
def totalProducts():
    try:
        cursor.execute("SELECT COUNT(*) FROM products;")
        result = cursor.fetchone()
        return result[0]
    except sqlite3.Error as e:
        print("Error while getting the total product number : ", e)


# endregion

# region Most expensive
def mostExpensive():
    try:
        cursor.execute("SELECT name, price FROM products ORDER BY price DESC LIMIT 1;")
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print("Error while getting the most expensive product : ", e)


# endregion

# region Leas expensive product
def leastExpensive():
    try:
        cursor.execute("SELECT name, price FROM products ORDER BY price ASC LIMIT 1;")
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print("Error while getting leas expensive product : ", e)


# endregion

# region Most common brand
def mostCommonBrand():
    try:
        cursor.execute("SELECT brand, COUNT(*) as count FROM products GROUP BY brand ORDER BY count DESC LIMIT 1;")
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print("Error while getting most common brand : ", e)


# endregion

# region Leas common brand
def leasCommonBrand():
    try:
        cursor.execute("SELECT brand, COUNT(*) as count FROM products GROUP BY brand ORDER BY count ASC LIMIT 1;")
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print("Error while getting leas common brand : ", e)


# endregion

# region Oldest product
def oldestProduct():
    try:
        cursor.execute("SELECT name, date_added FROM products ORDER BY date_added ASC LIMIT 1;")
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print("Error while getting oldest product : ", e)


# endregion

# region Newest product
def newestProduct():
    try:
        cursor.execute("SELECT name, date_added FROM products ORDER BY addedDate DESC LIMIT 1;")
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print("Error while getting newest product : ", e)


# endregion

# region Highest quantity product
def highestQuantity():
    try:
        cursor.execute("SELECT name, quantity FROM products ORDER BY quantity DESC LIMIT 1;")
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print("Error while getting highest quantity product: ", e)


# endregion

# region Lowest quantity
def lowestQuantity():
    try:
        cursor.execute("SELECT name, quantity FROM products ORDER BY quantity ASC LIMIT 1;")
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print("Error while getting lowest quantity product: ", e)


# endregion

# region Search product
def searchProductByName(name):
    try:
        query = "SELECT * FROM products WHERE name LIKE ?;"
        cursor.execute(query, ('%' + name + '%',))
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print("Error while searching product : ", e)


# endregion

# region Searching product brand
def searchProductByBrand(brand):
    try:
        query = "SELECT * FROM products WHERE brand LIKE ?;"
        cursor.execute(query, ('%' + brand + '%',))
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print("Error while searching product brand : ", e)
# endregion
