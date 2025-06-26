class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shopping_Cart:
    def __init__(self):
        self.items = []

    def add_products(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart")

    def remove_products(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"{product.name} removed from cart")
                return
        print("Product not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("Your cart contains:")
        for product in self.items:
            print(f"- {product.name}: ${product.price} x {product.quantity}")

    def total_price(self):
        total = sum(product.price * product.quantity for product in self.items)
        print(f"Total price: ${total}")

# Create product instances
p1 = Product("Laptop", 10000, 1)
p2 = Product("Mouse", 500, 2)

# Create shopping cart and add products
cart = Shopping_Cart()
cart.add_products(p1)
cart.add_products(p2)

# Use the shopping cart methods
cart.view_cart()
cart.total_price()
cart.remove_products("Mouse")
cart.view_cart()
cart.total_price()
