class Pizza(object):
    def __init__(self, size = "Small", crust = "regular", toppings = []):
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.cost = 0.0
        self.toppings = []
        self.completed = False

    def addToppings(self, topping):
        for x in self.toppAmount:
          self.toppings.append(x)

    def markedAsFinished(self):
        self.completed = True
        return self.comlpeted

    def formatPizza(self):
        return self.size + ", " + self.crust + ", " + str(self.toppAmount) + " Toppings: " + str(self.toppings)

    def cost(self,tops):
        if self.size == "small":
            self.cost = 5.50
        elif self.size =="medium":
            self.cost = 8.50
        else:
            self.cost = 11.25
        self.cost = self.cost + (tops * 1.00)
        return self.cost

class Order(object):
    def __init__(self, name = " ", phone = "123-111-1111"):
        self.name = name
        self.phone = phone

    def displayMenu(self):
        print("Welcome to the Pizza Shop.")
        print("Press P to place an order")
        print("Press M to modify the order")
        print("Press Q to quit the program ")
        print("Press E to enter employee program")


def main():
    orders = []
    p1 = Pizza("small", 4)
    orders.append(p1)
    p2 = Pizza("large", 2)
    orders.append(p2)
    for x in orders:
        print(x.formatPizza())



main()