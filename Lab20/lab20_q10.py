inventory = {
    "pen": (10.0, 50),
    "notebook": (45.0, 20),
    "eraser": (5.0, 100),
    "marker": (30.0, 15)
}

cart = {}

while True:
    item = input("Enter item name (or 'done' to finish): ").lower().strip()

    if item == "done":
        break

    if item not in inventory:
        print("Item not found!")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity! Please enter a whole number.")
        continue

    if quantity <= 0:
        print("Quantity must be positive.")
        continue

    price, stock = inventory[item]

    if quantity > stock:
        print("Insufficient stock!")
        continue

    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity

    inventory[item] = (price, stock - quantity)

    print("Item added to cart.")

subtotal = 0

for item, quantity in cart.items():
    price = inventory[item][0]
    subtotal += price * quantity

discount = 0

if subtotal > 500:
    discount = subtotal * 0.10

total = subtotal - discount

print("\n-------------------- RECEIPT --------------------")
print("Item".ljust(15), "Qty".rjust(5),
      "Price".rjust(10), "Total".rjust(10))
print("-" * 50)

for item, quantity in cart.items():
    price = inventory[item][0]
    line_total = price * quantity

    print(
        item.ljust(15),
        str(quantity).rjust(5),
        f"{float(price):.2f}".rjust(10),
        f"{float(line_total):.2f}".rjust(10)
        )

print("-" * 50)
print("Subtotal: ₹", round(subtotal, 2))
print("Discount: ₹", round(discount, 2))
print("Final total: ₹", round(total, 2))

print("\n------------- UPDATED INVENTORY -------------")

for item, (price, stock) in inventory.items():
    print(item, "| Price: ₹", price, "| Stock:", stock)

    if stock < 10:
        print("LOW STOCK!")