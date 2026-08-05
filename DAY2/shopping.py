cart = []
print("Welcome to shopping")
print("Enter the items. Type done when finished.")

while True:
    item = input("Enter item: ").strip()
    if item.lower() == "done":
        break
    if item:
        cart.append(item)

print("\nCart (list):", cart)
print("Cart type:", type(cart).__name__)

cart = tuple(cart)

print("Checkout")
print("Cart (tuple):", cart)
print("Cart type:", type(cart).__name__)
print("Total items:", len(cart))
