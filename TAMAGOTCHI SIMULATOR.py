# date: 04 - 21 -2023
# name: michelle lin
# purpose: to create a tamagotchi simulator using object oriented programming

# creating a class for item; which will be the items in store
class Item:
    def __init__(self, itemName, price, info, quantity):
        self.itemName = itemName
        self.price = price
        self.info = info
        self.quantity = quantity

    # making items printable using base overrides
    def __str__(self):
        return f'Item({self.itemName})'

    def __repr__(self):
        return self.__str__()

# creating a storefront class that contains the items that user can interact with
class Store:
    def __init__(self, inventory, money):
        self.inventory = inventory
        self.cart = []
        self.money = money
    def add_item(self, itemName, price, info, quantity):

        # polymorphism of add_item 
        self.inventory.add_item(itemName, price, info, quantity)

    def displayItems(self):
        items = self.inventory.get_item_list()
        print("Available items:")
        for item in items:
            print(f"{item.itemName}: ${item.price}")

    def buyItem(self, itemName):
        items = self.inventory.get_item_list()
        for item in items:
            if item.itemName == itemName:
                self.cart.append(item)
                print(f"{item.itemName} has been selected")

    def displayCart(self):
        print("items currently selected:")
        for item in self.cart:
            print(f"{item.itemName}: ${item.price}")
            total_cost = sum([item.price for item in self.cart])
            print(f"Total cost: ${total_cost}")

    def checkout(self):
        total_cost = sum([item.price for item in self.cart])
        if total_cost > self.money:
            print("not enough funds!")
        else:
            self.money -= total_cost
            self.cart = []
            # calculating the money leftover after purchase
            print(f"money available: ${self.money}")
            print("thank you for your purchase, please come again soon")

# creating inventory class that stores the items a user has bought from the storefront such that user is able to use these items on their pet
# has multiple inheritance, accessing item and store classes
class Inventory(Item, Store):
    def __init__(self):
        self.__item_list = [] #encapsulation of item_list
        self.cart = []

    def add_item(self, itemName, price, info, quantity):
        current_item = Item(itemName, price, info, quantity)
        self.__item_list.append(current_item) 

    def add_cart_items(self, cart):
        for item in cart:
            self.cart.append(item)
    
    def get_item_list(self):
        return self.__item_list

    # was trying to get this to interact with the cart from store, but was not successful
    def get_cart_items(self):
        return self.cart

    # base override that allows us to iterate our inventory
    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        self.__index += 1 
        
        if self.__index >= len(self.__item_list):
            self.__index = -1 
            raise StopIteration 
        else:
            current_item = self.__item_list[self.__index]
            return current_item

    # base override allowing us to make inventory printable
    def __str__(self):
        return f"inventory({self.__item_list}, {self.cart})"

    def __repr__(self):
        return self.__str__()

# pet class that was supposed to be like a little tamagotchi experience;; basically copied and pasted from class example :) work smarter not harder yknow!!
class Pet:

    def __init__(self, name):
        self.name = name
        self.is_hungry = False
        self.is_tired = False
        self.play = False

    def eat(self):
        if self.is_hungry:
            print(
                f'{self.name} is eating {self.get_item_list}!')
            self.is_hungry = False
            return True
        else:
            print(f'{self.name} is not hungry right now :C.')
            return False

    def sleep(self):
        if self.is_tired:
            print(f'{self.name} is sleeping zzz.')
            self.is_tired = False
            return True
        else:
            print(f'{self.name} is not tired.')
            return False

    def play(self):
        if self.play:
            print(
                f'{self.name} is playing with {self.get_item_list}!')
            self.play = False
            return True
        else:
            print(f'{self.name} is too tired to play right now :C.')
            return False

    def __str__(self):
        return f'Animal named: {self.name}.'

    def __repr__(self):
        return self.__str__()
