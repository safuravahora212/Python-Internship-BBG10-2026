inventory = {"pen": 10, "notebook": 5, "eraser": 20}

# 1. Navo stock add karvo
inventory["pencil"] = 15
print("After adding:", inventory)

# 2. Item sell thayo to stock ochu karvo
item_to_sell = "pen"
if item_to_sell in inventory:
    inventory[item_to_sell] -= 1
    print(item_to_sell, "sold!")
else:
    print(item_to_sell, "not found!")

# 3. Je item che j nahi e vechva try karyu to
item_to_sell = "scale"
if item_to_sell in inventory:
    inventory[item_to_sell] -= 1
else:
    print(item_to_sell, "does not exist in inventory!")

print("Final inventory:", inventory)