menu = {
    'Coffee': 60, 'Tea': 55, 'Pizza': 80, 'Burger': 90, 'Chickenpuff': 70
}

print("Welcome to TOWN CAFE")
print("Coffee: 60\nTea: 55\nPizza: 80\nBurger: 90\nChickenpuff: 70")

order_total = 0

# first input
items = input("Enter items: ").split()

for item in items:
    if item in menu:
        order_total += menu[item]
    else:
        print(f"{item} is not available")
print(f"Bill: {order_total}")

# ask only once
order = input("Do you want anything else (Yes/No): ")

if order.lower() == "yes":
    items2 = input("Enter items: ").split()

    for item2 in items2:
        if item2 in menu:
            order_total += menu[item2]
        else:
            print(f"{item2} is not available")

print(f"Total Bill: {order_total}")
