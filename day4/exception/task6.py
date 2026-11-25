def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
    except KeyError:
        print("Error: Missing 'item' or 'price' key!")
    else:
        print(f"Order: {item}, Price: {price}")
    finally:
        print("Processing complete")

process_order({"item": "Pizza", "price": 250})

print("---")

process_order({"item": "Burger"})