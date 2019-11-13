#Basilio Bazan III
#bb36366

def getGuessFromUser():
    userguess = input("Guess: ")
    return userguess

def displayFeedback(feedback):
    print("Feedback: {0}{1}{2}{3}".format(feedback[0], feedback[1], feedback[2], feedback[3]))

def checkError(string1):
    acceptable = ["R", "G", "P", "Y", "B", "O"]
    error = False

    if len(string1) > 4 or len(string1) < 4:
        error = True

    for a in string1:
        if a not in acceptable:
            error = True
    return error

def errorMessage():
    print("Error")

def finalScoreCodebreaker(numOfTurns):
    print("Score: -{0}".format(numOfTurns))

def codeMaster(lock,four):
    new = ["","","",""]
    temp = []
    for y in lock:
        temp.append(y)

    for a in range(4):
        if temp[a] == four[a]:
            new[a] = four[a]
            temp[a] = "X"
            four[a] = "Z"

    for b in range(4):
        if four[b] in temp:
            new[b] = "W"
            for z in range(4):
                if temp[z] == four[b]:
                    temp[z] = "X"
                    break

    for c in range(4):
        if new[c] == "":
            new[c] = "_"

    return new

def main():
    file = open("input.txt", "r")
    for x in file:
        score = 0
        code = []
        for i in x.strip("\n"):
            code.append(i)

        while score < 10:
            guess = getGuessFromUser()
            four = []
            for y in guess:
                four.append(y)

            if checkError(four):
                errorMessage()
            else:
                feedback = codeMaster(code, four)
                displayFeedback(feedback)

                if feedback == code:
                    score += 1
                    break
                score += 1
        finalScoreCodebreaker(score)
    file.close()

main()