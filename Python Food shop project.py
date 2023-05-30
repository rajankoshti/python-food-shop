#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Welcome message
print("Welcome to our food shop! We have the following items on our menu:")

# Menu
menu = {
    "Burger": 50,
    "Fries": 40,
    "Pizza": 100,
    "Cold drink": 20,
    "Shake": 50
}

for item, price in menu.items():
    print(f"{item} - Rs {price}")

# Take order
order = {}
total = 0

while True:
    item = input("Please enter an item from the menu (or 'done' to finish): ")
    if item == "done":
        break
    elif item not in menu:
        print("Sorry, that item is not on the menu.")
        continue

    quantity = int(input(f"How many {item}s would you like? "))
    order[item] = quantity
    total += quantity * menu[item]

# Eating option
print("Thank you for your order!")
eating_option = input("Would you like to eat here or home delivery (15% delivery charge)? ")

# Bill
if eating_option == "eat here":
    print("\nHere is your bill:")
    for item, quantity in order.items():
        print(f"{item} x {quantity} = Rs {menu[item] * quantity}")
    print("Total = Rs", total)
else:
    total *= 1.15 # Add 15% delivery charge
    print("\nHere is your bill:")
    for item, quantity in order.items():
        print(f"{item} x {quantity} = Rs {menu[item] * quantity}")
    print("Delivery charge (15%) = Rs", round(total*0.15))
    print("Total = Rs", round(total, 2))

# Thank you message
print("\nThank you for visiting our food shop! Please come again.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




