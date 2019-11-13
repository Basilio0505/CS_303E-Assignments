#Basilio Bazan (bb36366)
#Eduardo Alvarez (eja779)

'''Will be used to randomly choose the damage in combat'''
import random

def hitEnter():   #Function Definition and Function Call
    print("")   #print() statement
    raw_input("[Hit Enter] ")

'''Shop for the user to spend his currency to get new weapons'''
def shop(player):
    while True:   #While Loop
        try:   #Try and Except Block
            hitEnter()   #A Function that calls another Function (main not included)
            print("-----------------------------------------------")
            print("[0}-Nothing------------------------------------")
            print("[1]-High Powered Pistol---------3dmg--25 silver")
            print("[2]-Shotgun---------------------4dmg--50 silver")
            print("[3]-Winchester Rifle------------6dmg--75 silver")
            print("[4]-Heal (1 Health)--------------------5 silver")
            print("-----------------------------------------------")
            print("Your money balance: "+ str(player.getMoney()))
            item = raw_input("Enter Number --> ")
            if item == 0:   #If Statement and Assigment Statement
                print("")
            elif item == 1:
                if player.getMoney() >= 25:   #Nested If Statement
                    print("You purchased the High Powered Pistol.")
                    player.spendMoney(25)
                    player.changeGun("High Powered Pistol")
                else:
                    print("You don't have enough to purchase this item")
            elif item == 2:
                if player.getMoney() >= 50:
                    print("You purchased the Shotgun.")
                    player.spendMoney(50)
                    player.changeGun("Shotgun")
                else:
                    print("You don't have enough to purchase this item")

            elif item == 3:
                if player.getMoney() >= 75:
                    print("You purchased the Winchester Rifle")
                    player.spendMoney(75)
                    player.changeGun("Winchester Rifle")
                else:
                    print("You don't have enough to purchase this item")

            elif item == 4:
                if player.getMoney() >= 5:
                    print("You purchased a Heal")
                    player.spendMoney(5)
                    player.heal()
                else:
                    print("You don't have enough to purchase this item")
            else:
                item = "invaild"
                item = int(item)
            while True:
                try:
                    again = raw_input("\nWould you like to purchase another item? [1]yes/[2]no    Enter number-->")
                    if again ==1:
                        print("")
                    elif again ==2:
                        print("")
                    else:
                        again = "invaid"
                        again - int(again)
                    break
                except:
                    print("Oops! That input was invalid. Please try again.")
            if again == 2:
                break
        except:
            print("Oops! That input was invalid. Please Try again.")

'''How the user is able to traverse the world'''
def travel(world, index):   #Function Definition with Default Parameters and Function Call
        while index < 0 or index >= len(world):
            print(world)
            action = raw_input("Where would you like to go next? -->").lower()
            for a in range(len(world) - 1):   #For Loop
                if world[a] == action:
                    index = a
                    break
            if index >= 0 and index < len(world):
                print("going to " + str(world[index]))
                break
            print("Opps that's not a valid location. Try again")
            print("")
        return index

'''How the combat is implemented'''
def fight(friends, number):
    enemies = {}   #Dictionary
    for x in range(1,number+1):
        enemies["enemy" + str(x)] = 10
    print(enemies)
    while len(enemies) > 0:   #Nested Loops
        for a, b in enemies.items():
            if len(friends) == 0:
                print("EVERYONE IS DEAD. GAME OVER.")
                break
            rnum = random.randint(0,len(friends)-1)   #Random Number Generator
            print(str(a)+" hit "+ friends[rnum].getName())
            friends[rnum].hit(2)
            if friends[rnum].getHealth() <=0:
                print("Oh NO! "+friends[rnum].getName()+" is dead!!")
                friends.remove(friends[rnum])
                for x in friends:
                    print(x.getName())
            hitEnter()

        for z in friends:
            if len(enemies) == 0:
                break
            shot = "enemy" + str(len(enemies))
            print(str(z.getName()) + " hit " + shot)
            enemies[shot] -= z.weapondamage()
            print(shot + "'s health is at " + str(enemies[shot]))
            if enemies[shot] <= 0:
                print(shot + " is dead!")
                del enemies[shot]
            hitEnter()

'''Keeps all the user's stats, inventory, currency, etc.'''
class Character(object):   #Class
    def __init__(self, name = "Deputy", weapon = "Basic Revolver", money = 20):
        self.health = 10
        self.name = name
        self.weapon = weapon
        self.money = money

    def weapondamage(self):
        damage = 1
        if self.weapon == "Basic Revolver":
            damage = 2
        if self.weapon == "High Powered Pistol":
            damage = 3
        if self.weapon == "Shotgun":
            damage = 4
        if self.weapon == "Winchester Rifle":
            damage = 6
        return damage

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getMoney(self):
        return self.money

    def displayHealth(self):
        print(self.name +"'s health is: "+str(self.health)+"/10")

    def changeGun(self, weapon):
        self.weapon = weapon

    def heal(self):
        self.health += 1   #Use of +=, -=, etc.

    def hit(self, damage):
        self.health -= damage
        if self.health > 0:
            self.displayHealth()

    def addMoney(self,found):
        self.money += found
    def spendMoney(self,found):
        self.money -= found


def main():
    '''Introduction'''
    print("You arrive to the town of Tumbleweed where you have been stationed as their new sheriff")
    print("You hitch your horse at the local jailhouse and step inside to be greeted by a young deputy.")
    hitEnter() #Function definition and Function Call
    name = raw_input("?:\"Hello new sheriff what is your name\"--> ")
    print("?:\"Welcome Sheriff " + name + " to the town of Tumbleweed\"")
    print("?:\"Thanks for coming to help us clear up the gang presence and put a stop to their leader Cactus Dan.\"")
    print("Carson:\"I'm Deputy Carson and I'll help you stop this menace.\"")
    player = Character(name)
    carson = Character("Carson","High Powered Pistol")
    hitEnter()
    print("Both you and your Deputy exit the building and are now outside")
    print("Carson:\"Well partner here take these starting items\"")
    print("YOU RECEIVED \"Basic Revolver\" & \"20 Silver\"")
    hitEnter()
    print("Carson:\"Well partner we should go around town to get some leads and maybe find some of Cactus Dan's men.\"")
    hitEnter()

    '''List for environment'''
    world = ["saloon", "bank", "street", "store"]
    '''List of allies'''
    posse = [player, carson]
    index = len(world)
    index = travel(world, index)   #Function Definition with Default Parameters and Function Call
    hitEnter()

    '''All possible scenerios in all locations user can experience'''
    loop = 100
    while loop == 100:
        loop = index

        while loop == 0:
            print("You arrive at the saloon.")
            print("Upon entering you study the room. There is a long bar where you see a BARTENDER cleaning glasses.\n"
                  "At the bar you also spot a young COUPLE enjoying a couple of drinks. In the middle of the room \n"
                  "you spot a group of GAMBLERS clearly drunk. And in the corner of the room you spot a MAN leaning\n"
                  "up against the wall.")
            hitEnter()
            print("You walk up to the bar and is greeted by the Bartender.")
            print("Bartender:\"Howdy, sheriff you got some balls stopping by here since the previous sheriff"
                  " died here.\"")

            hitEnter()
            print("You approach the young couple at the bar and greet them.")
            print("As they turn to you notice they are in their twenties dressed as if they are from a bigger city \n"
                  "rather than the small desert town you guard over. The young man wears a grey suit while the woman\n"
                  "is in a white dress.")
            hitEnter()
            print("Young Man: \"Well hello sheriff, me and the misses here just got married and me and my wife \n"
                  "Delilah decided to stop by and enjoy some drinks.")
            print("Young Lady: \"Unfortunately our parents own rival businesses so us being together was not approved\n"
                  "and rather than being away from each other me and Jack decided to escape the city life and live on\n"
                  "our own in the wild west.")
            hitEnter()

            while True:
                try:
                    ask1 = int(raw_input("[1](Buy them a couple drinks)/[2](You remember seeing her missing poster "
                                     "and want to take them in)\nEnter Number --> "))
                    if ask1 == 1:
                        print("\nJack:\"Well we definitely appreciate that sheriff "+player.name+" it sure is tough \n"
                              "out here but at least we have each other.\"")
                        print("Delilah:\"Thank You Sheriff "+player.name+"\"")
                        print("You spent 2 silver")
                        player.spendMoney(2)
                    elif ask1 == 2:
                        print("\nBefore you can react Delilah splashes her glass of alcohol in your eyes. And when you\n"
                              "clear your sight you find both of them have fled.")
                    else:
                        ask1 = "invaild"
                        ask1 = int(ask1)
                    break
                except:
                    print("Oops! That input was invalid. Please Try again.")

            hitEnter()
            print("You notice that the man in the corner still has not moved from his location.")
            print("He seems to be staring intently at the three drunk gang members at the table.")
            hitEnter()

            while True:
                try:
                    ask2 = int(raw_input("[1](Call him out)/[2](Leave him be)    Enter Number --> "))
                    if ask2 == 1:
                        print("He notices you starting your approach and decides to leave the saloon and you return\n"
                              "to the bar.")
                    elif ask2 == 2:
                        print("You ignore the man as he seems not to be doing anything wrong.")
                    else:
                        ask2 = "invaild"
                        ask2 = int(ask2)
                    break
                except:
                    print("Oops! That input was invalid. Please Try again.")

            hitEnter()
            print("Suddenly the three men sitting at the table finally notice you and draw their weapons!")
            print("Gang Member: \"Cactus Dan said no man of the law is allowed in this saloon and now you will pay\n"
                  "with you life. I can't wait to tell Cactus Dan back at the MANSION.\"")
            print("As shots begin to be fired at you and Carson duck behind the bar.")
            world.append("Mansion")
            if ask1 == 1 and ask2 == 1:
                hitEnter()
                print("In the crossfire Jack is shot in the head!!")
                print("Delilah ducks behind the bar and pulls out a shotgun that was strapped to her leg.")
                print("She fires back and instantly kills one of the men.")
                delilah = Character("Delilah","Shotgun")
                posse.append(delilah)
                hitEnter()
                fight(posse, 2)
                hitEnter()
                if player.getHealth() <= 0:
                    loop = 321
                    break
            if ask1 == 2 and ask2 == 2:
                hitEnter()
                print("From behind the group of men the lonely stranger flips a table and shoot at the men instantly\n"
                      "killing one of them with his revolver.")
                print("Looks like he's on your side.")
                stranger = Character("Stranger", "Basic Revolver")
                posse.append(stranger)
                hitEnter()
                fight(posse, 2)
                hitEnter()
                if player.getHealth() <= 0:
                    loop = 321
                    break
            if ask1 == 2 and ask2 == 1:
                hitEnter()
                print("You and Carson draw your weapons and begin to fight back.")
                hitEnter()

                fight(posse, 3)
                hitEnter()
                if player.getHealth() <= 0:
                    loop = 321
                    break
            if ask1 == 1 and ask2 ==2:
                hitEnter()
                print("In the crossfire Jack is shot in the head!!")
                print("Delilah ducks behind the bar and pulls out a shotgun that was strapped to her leg.")
                print("She fires back and instantly kills one of the men.")
                delilah = Character("Delilah","Shotgun")
                posse.append(delilah)
                hitEnter()
                print("From behind the group of men the lonely stranger flips a table and shoot at the men instantly\n"
                      "killing one of them with his revolver.")
                print("Looks like he's on your side.")
                stranger = Character("Stranger", "Basic Revolver")
                posse.append(stranger)

                hitEnter()
                fight(posse, 1)
                hitEnter()
                if player.getHealth() <= 0:
                    loop = 321
                    break

            print("You acquire 50 gold after the shootout")
            player.addMoney(50)
            hitEnter()
            loop = travel(world, len(world))

        while loop == 1:
            print("You arrive at the city bank.")
            print("Before entering you notice two suspicious guys hanging out near the bank but think nothing of it.\n"
                  "As you enter the bank you notice everything is operating as usual. The Bank manager is assisting\n"
                  "a customer in his office and the employees are working as they should. Outside the bank managers\n"
                  "you notice a guy standing guard with a shotgun.")
            hitEnter()

            print("As the bank manager finishes with his client, he comes up to you and greets you with a big firm\n"
                  "handshake.")
            print("Bank manager: \"Well I'll be damned if it isn't the new sheriff!\"")
            hitEnter()

            print("The Bank manager introduces you to his personal bodyguard called Billy.")
            print("Billy:\"Howdy\"")
            print(
                "Billy:\"Just between me and you, I don't like that annoying bank manager but he does pay well and I\n"
                "could use the money.\"")
            hitEnter()

            print("Suddenly two men come bursting through the doors heavily armed shooting up the place...")
            hitEnter()

            while True:
                try:
                    ask1 = int(raw_input("[1](Jump behind cover)/[2](Push Billy to cover taking some damage)"
                                     "\nEnter number --> "))
                    if ask1 == 1:
                        print("Billy was shot but able to make it to cover.")
                    elif ask1 == 2:
                        print("You take 1 damage.")
                        player.hit(1)
                        print("Billy:\"Thanks sheriff! That was a close one!\"")
                    else:
                        ask1 = "invalid"
                        ask1 = int(ask1)
                    break
                except:
                    print("Oops! That input was invalid. Please try again.")

            hitEnter()

            print("You notice the bank manager has made it behind cover but is screaming for help as well as his \n"
                  "workers.")
            print("Robbers:\"We already told that bank manager that this money belongs to our gang!\"")
            hitEnter()
            print("Billy:\"We need to protect them!\"")

            while True:
                try:
                    ask2 = int(raw_input("[1](Save the workers first)/[2](Try to fight the two robbers by yourself while "
                                     "Billy saves everyone)\nEnter number --> "))
                    if ask2 == 1:
                        print("Billy is able to secure the hostages to a safe place while you cover him in the shootout")
                    elif ask2 == 2:
                        print("You are able to kill one of the robbers but in consequence one of the workers dies\n"
                            "causing Billy to be mad at you.")
                    else:
                        ask2 = "invalid"
                        ask2 = int(ask2)
                    break
                except:
                    print("Oops! That input was invalid. Please try again.")

            hitEnter()
            if ask1 == 1 and ask2 == 1:
                print("Billy will now join you in the shootout and all the civilians escape safely")
                print("Billy is thankful for helping save the workers and will join you in your quest although wounded.")
                billy = Character("Billy", "Shotgun")
                billy.hit(2)
                posse.append(billy)
                hitEnter()
                fight(posse, 2)
                if player.getHealth() <= 0:
                    loop = 321
                    break
                hitEnter()
            if ask1 == 2 and ask2 == 2:
                print("You have taken some damage but able to fight off the robbers without anyone else getting hurt.")
                hitEnter()
                fight(posse, 1)
                if player.getHealth() <= 0:
                    loop = 321
                    break
                hitEnter()
                print("Billy is thankful for saving him but does not trust you to enough to join you in your quest.")
                hitEnter()
            if ask1 == 2 and ask2 == 1:
                print("You and Billy are able to ensure the safety of the civilians in the bank.")
                print("Billy seems to trust you and decides to join your cause to finish this gang and will help you \n"
                      "in this fight.")
                billy = Character("Billy", "Shotgun")
                posse.append(billy)
                hitEnter()
                fight(posse, 2)
                if player.getHealth() <= 0:
                    loop = 321
                    break
                hitEnter()
            if ask1 == 1 and ask2 == 2:
                print("You are able to kill one of the robbers but at the cost of innocent lives.")
                print("Billy is shot in the head by the other robber!!")
                hitEnter()
                fight(posse, 1)
                if player.getHealth() <= 0:
                    loop = 321
                    break
                hitEnter()

            print("You acquire 50 gold after the shootout")
            player.addMoney(50)
            hitEnter()
            loop = travel(world, len(world))

        while loop == 2:
            print("You arrive at the city main street.")

        while loop == 3:
            print("You arrive at the mansion.")

        while loop == 4:
            print("You arrive at the store.")
            print("An elderly lady stands at the counter and gives you a big smile.")
            print("Shopkeeper:\"Welcome young man what are you interested in buying today?\"")
            shop(player)
            hitEnter()
            loop = travel(world, len(world))

        loop = 100
main()