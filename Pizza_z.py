

import sys
import random

class Pizza(object):
    def __init__(self, size = "small", crust = "regular", toppings = []):
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.completed = False

    def formatPizza(self):
        return self.size + " " + self.crust

    def addToppings(self, toppings):
        for x in toppings:
            self.toppings.append(x)

    def markedAsFinished(self):
        self.completed = True

class Order(object):
    def __init__(self, name = "", phoneNumber = "555-555-5555", pizzas = []):
        self.name = name
        self.phoneNumber = phoneNumber
        self.pizzas = pizzas
        self.number = random.randint(0, 10000)

    def displayOrder(self):
        for x in self.pizzas:
            print(x.formatPizza())

    def addPizza(self, addedPizza):
        self.pizzas.append(addedPizza)

    def formatOrder(self):
        allPizzas = ""
        for x in self.pizzas:
            print(x)
            #allPizzas += x.formatPizza()
        return str(self.number) + ", " + self.name + ", " + self.phoneNumber + ": " + allPizzas

    def completeOrder(self):
        for x in self.pizzas:
            print(x)
            #x.markedAsFinished()

def displayMenu():
    print("Welcome to the Pie in the Sky Pizza Shoppe")
    print("Enter P to place an order")
    print("Enter M to modify an order")
    print("Enter Q to quit the program")
    print("Enter E to enter employee part of program")

def getToppings():
    toppings = []
    options = ["Mushrooms", "Green Olives", "Tomatos", "Green Peppers", "Extra Cheese"]

    while(True):
        for x in range(len(options)):
            print("(" + str(x + 1) + ") " + options[x])

        top = eval(input("Enter topping number or negative if done: "))
        if(top < 0):
            return toppings
        else:
            toppings.append(options[top-1])


def displayPizzaMenu():
    size = input("What size of pizza would you like to order? Small, Medium, or Large")
    crust = input("What type of crust would you like to order? Thin, Regular, or Chicago")
    toppings = getToppings()
    pizzaOrder = Pizza(size, crust, toppings)
    return pizzaOrder


def modifyingAnOrder(currentOrder):
    while (True):
        pizzasOrdered = []
        pizzaOrdered = displayPizzaMenu()
        pizzasOrdered.append(pizzasOrdered)
        continueOrdering = input("Enter Y to order another pizza, N to stop: ")
        if (continueOrdering[0] == 'N' or continueOrdering[0] == 'n'):
            return currentOrder
        else:
            pizzaOrdered = displayPizzaMenu()
            currentOrder.addPizza(pizzasOrdered)


def displayOrderScreen():

    name = input("Please enter your name: ")
    phoneNumber = input("Please enter your phone number: ")

    while (True):
        pizzasOrdered = []
        pizzaOrdered = displayPizzaMenu()
        pizzasOrdered.append(pizzasOrdered)
        currentOrder = Order(name, phoneNumber, pizzasOrdered)
        continueOrdering = input("Enter Y to order another pizza, N to stop: ")
        if (continueOrdering[0] == 'N' or continueOrdering[0] == 'n'):
            return currentOrder
        else:
            pizzaOrdered = displayPizzaMenu()
            currentOrder.addPizza(pizzasOrdered)


    #currentOrder.addPizza(p)


def main():
    allOrders = []

    while(True):
        displayMenu()
        userInput = input("")
        userInput = userInput.upper() #so it will convert to uppercase either way

        if userInput == "Q":
            sys.exit(0)
        elif userInput == "P":
            print("Order Screen coming up...")
            order = displayOrderScreen()
            allOrders.append(order)
            print("Your order number is: " + str(order.number))
        elif userInput == "M":
            userNumber = eval(input("Please provide your order number:"))
            for x in allOrders:
                if(userNumber == x.number):
                    print("Found it!")
                    modifyingAnOrder(x)
                #else: #Debugging statement
                #    print("Not found :-( Sorry.")
        elif userInput == "E":
            print("All current orders: ")
            for x in allOrders:
                print(x.formatOrder())
            orderNumber = eval(input("Please provide your order number:"))
            for x in allOrders:
                if(orderNumber == x.number):
                    print("Found it!")
                    x.completeOrder()
                #else: #Debugging statement
                #    print("Not found :-( Sorry.")


main()
