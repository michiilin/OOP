from pet import Store, Inventory, Pet

 # create an inventory object
inventory_obj = Inventory()

# create a store object with the inventory object
store_obj = Store(inventory_obj, 666.0)

def storefront():

    print("\nyou selected store! here are the things on sale:")
    print(f"money available: ${store_obj.money}\n")

    # add some items to the store
    store_obj.add_item("1. kibble", 10.0, "crunchy squares", 5)
    store_obj.add_item("2. raw food", 50.0, "bouhjee food", 3)
    store_obj.add_item("3. snack", 5.0, "smol food", 10)
    store_obj.add_item("4. ball", 2.0, "round circle go boing boing", 10)
    store_obj.add_item("5. towel", 1.0, "for some reason dogs really love shredding these", 10)

    
    # display the available items for sale
    store_obj.displayItems()

    # buy an item and add it to the cart
    user_input = input("enter name of item you want to buy: ")
    
    store_obj.buyItem(user_input)

    # display the items in the cart
    store_obj.displayCart()
    inventory_obj.add_cart_items

def selfInventory(inventory_obj):
    print("you selected inventory! here are the things in your inventory:")
for item in inventory_obj.get_item_list():
    print(f'{item.itemName} - ${item.price} - {item.info} - {item.quantity} pcs')
print(f'cart: {",".join([item.itemName for item in inventory_obj.get_cart_items()])}')

def petCare():
    print("you selected pet! select one of the following to care for your pet:")
    print("0. customize your pet")
    print("1. feed")
    print("2. sleep")
    print("3. play")
    print("4. quit")

    choice = input("Enter your choice: ")

    if choice == "0":
        createPet = (input("what type of pet do you want? "))
        Pet.name = (input("give your pet a name: "))
        createPet = Pet(Pet.name, inventory_obj)
        print(createPet)
        
    elif choice == "1":
        print("you have selected to feed your pet! choose a food from your inventory below: \n")
        Inventory.get_item_list
    
    elif choice == "2":
        print("you have selected to put your pet to sleep!")

    elif choice == "3":
        print(
            "you have selected to play with your pet! choose an item from your inventory to play with your pet: "
        )
    elif choice == "4":
        print("sad")


while True:
    print('\nwelcome to the menu! choose an option below:')
    print("1. store")
    print("2. inventory")
    print("3. pet")
    print("4. quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        storefront()

    elif choice == "2":
       selfInventory(inventory_obj)

    elif choice == "3":
        petCare()

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid number.")
        break
