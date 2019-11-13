#def main():
#    print("Hello World")
#def addThreeValues(x,y,z):
#    return x+y+z

#def displayUserMenu():
#    print("Enter D to display all student grades")
#    print("Enter A to display the class average")
#    print("Enter E to exit")

#def getArea(length, width):
#    return length * width

#def main():
#    x = addThreeValues(3,4,2)
#    print(x)
#    area = getArea(10,5)
#    print(area)
#    displayUserMenu()
#    print("Program Complete")

#class Cookie(object):
#    def __init__(self):
#        self.type = "unknown"
#        self.ingrediantList = []
#        self.size = "medium"
#    def __init__(self,type,size):
#        self.type = type
#        self.size = size

#    def calculateCost(self,number):
#        #it is 15 cents per cookie to make
#        return 0.15* number

#    def calculateCost2(self,number):
#        if self.size == "medium":
#            return 0.15 * number
#        elif self.size == "large":
#            return 0.25 * number
#        else:
#            return 0.10 * number

#class Fraction(object):
#    def __init__(self, n, d):
#        self.n = n
#        self.d = d

#    def addFraction(self, f1):
#        commond = self.d *f1.d
#        top = (self.n * f1.d) + (f1.n * self.d)
#        return Fraction(top, commond)

#    def multFraction(self, f1):
#        return Fraction(self.n * f1.d, f1.n * self.d)

#    def displayNice(self):
#        return str(self.n) + "/" + str(self.d)


def swapTwoV2(index1, index2, alist):
    temp = alist[index1]
    alist[index1] = alist[index2]
    alist[index2] = temp

def selectSort(alist):
    for x in range(0,len(alist)):
        temp = alist[x]
        for y in range(x,len(alist)):
            if temp > alist[y]:
                temp = alist[y]
                alist[y] = alist[x]
                alist[x] = temp

def bubbleSort(alist):
    count = -1
    while count != 0:
        count = 0
        for x in range(0,len(alist)-1):
            if alist[x] > alist[x+1]:
                temp = alist[x]
                alist[x] = alist[x+1]
                alist[x+1] = temp
                count += 1

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def main():
#    c1 = Cookie("Chocolate Chip", "large")
#    print(c1)
#    print(c1.type)
#    print(c1.size)
#    cost = c1.calculateCost2(24)
#    print("Total Cost = " + str(cost))
#    fraction1 = Fraction(1,4)
#    fraction2 = Fraction(1,2)
#    fraction3 = fraction1.addFraction(fraction2)
#    print(fraction3.displayNice())
#    print(fraction1.multFraction(fraction2).displayNice())
#    mylist = [0, 2, 1, 3, 4, 5]
#    print(mylist)
#    swapTwoV2(1,2,mylist)
#    print(mylist)
    #mylist = [24,6,54,45,67,82,10]
#    selectSort(mylist)
#    print(mylist)
    #bubbleSort(mylist)
    #print(mylist)
    alist = [54,26,93,17,77,31,44,55,20]
    insertionSort(alist)
    print(alist)

main()