def add_item(menu, item):
    menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"Error: {item} is not on the menu.")

def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item_name = "Tacos"
remove_item_name = "Salad"
check_item_name = "Pizza"

add_item(initial_menu, add_item_name)

remove_item(initial_menu, remove_item_name)

availability_message = check_item(initial_menu, check_item_name)

print(f"Updated menu: {initial_menu}")
print(f"Availability: {availability_message}")
