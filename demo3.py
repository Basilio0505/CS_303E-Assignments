def main():
    #Open file
    #file = open("something.txt", "r") #r=read a=append w=write
    #nameoffile = "input.txt"
    #file1 = open(nameoffile, "w")
    #stuff= ["hi\n","hey\n", "yo\n", "what do?\n", "what up?\n", "howdy\n", "hola\n", "bonjour\n", "hello\n", "ciao"]
    #stuff = ["hi", "hey", "yo", "what do?", "what up?", "howdy", "hola", "bonjour", "hello", "ciao"]

    #file1.writelines(stuff)
    #for x1 in stuff:
    #    file1.write(x1)

    #lines = file.readLines()
    #print(lines)

    #for x in range(7):
    #    print(file.readLine().strip("\n"))
    #for x in file:
    #    print(x.strip("\n"))

    #file.close()
    #file1.close()
    ############################################################################################
    #tuples are immutable
    #tuple1 = ("hello", "goodbye", 1776, 42)
    #print(tuple1[0])
    #total = tuple1[2] + tuple1[3]
    #print(total)
    #print(tuple1)

    #numbers = (1,2,3,4,5,6,7,8)
    #print(numbers[2:5])
    #newTutple = tuple1 + numbers
    #print(newTutple)

    #print(len(newTutple))
    #t1 = (1,2,3)
    #t2 = (2,3,4)
    #print(max(t1))
    #if cmp(t1,t2) == 0:
    #    print("match")
    #else:
    #    print("not match")

    #tNew = tuple([1,2,"hello",3])
    #print(tNew)
    #lNew = list(tNew)
    #print(lNew)
    #######################################################################
    #Sets
    #x = set([1,2,3,4,5,6,7])
    #y = {1,2,3,4,5}
    #print(x.difference(y))
    #print(y.issubset(x))
    #print(x.intersection(y))
    #print(x.union(y))
    #x.add(8)
    #print(x)

    #w = {"a", "b", "c"}
    #w.add("d")
    #print(w)
    #w.add("e") #Hashed into its location
    #print(w)
    #w.remove("b")
    #print(w)

    #######################################################################################
    #Format Method
    #num1 = 3.142565874
    #num2 = 10.5634743
    #print("num1 is {0} and num2 is {1}".format(num1,num2))
    #print("num1 is {0:.3} and num2 is {1:.3}".format(num1, num2))
    #print("num1 is {0:.3f} and num2 is {1:.3f}".format(num1, num2))

    # F-String mathod
    #print(f"num1 is {num1} and num2 is {num2}")
    #print(f"num1 is {num1:.4f} and num2 is {num2:.4f}")
    #####################################################################################
    #Try/Except Block
    #A method that allows a program to deal with any exceptions that
    #occur and then continue with normal program execution.
    #Exception: Error that occurs during runtime of a program
    #Stack Traceback: long error message you see when trying to run
    #try:
    #    x=42
    #    y=2
    #    result= x / y
    #    print(result)
    #except ZeroDivisionError:
    #    print("oops! you tried to divide by zero")
    #    result = 1
    #except:
    #    print("oops! error occured")
    #    result = 1
    #print(result)

    #try:
    #    x=0
    #    while(x<1 or x>5):
    #        x = int(input("Please enter a 1,2,3,4, or 5: "))
    #        break
    #except NameError:
    #    print("Oops! That is a word! "
    #          "Please try to do it right...")
    #except ValueError:
    #    print("Oops! That is a word! "
    #          "Please try to do it right...")
    #except:
    #    print("Not a valid number try again...")
    #finally:
    #    print("Well hello finally")
############################################################################
    #students = {"john": 3, "peter": 2}
    #students["susan"] = 5
    #print(students)
    #students["peter"] = 5
    #print(students)
    #students["peter"] += 5
    #print(students)

    #sum = 0
    #for x in students.values():
    #    sum += x
    #    print("avg = " + str(sum / len(students)))
    #students.clear()

    #for k, v in students.items():
    #    print(k, v)
    #d1 = {"red":41, "blue":3, "green":87}
    #print(d1)
    #print(d1.items())
    #print(d1.keys())
    #print(d1.values())
    #print(len(d1))
    #print(d1["red"])
    #d1["green"] = 99
    #print(d1["green"])
#######################################################################################
    cast = {"Ned", "Chuck", "Emerson", "Olive", "Vivian", "Lily"}
    detective = {"Emerson", "Ned"}
    aunts = {"Vivian", "Lily"}
    print(cast.difference(detective).difference(aunts))
    print(cast.intersection(aunts))
    print(cast.union(aunts))

main()