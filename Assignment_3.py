fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 0:
        value = 0
    elif n == 1:
        value =1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value

def main():
    num = 0
    while num >= 0:
        asciivals = []
        phrase = input("")
        num,semi, word = phrase.partition(";")
        num = int(num)
        if num < 0:
            break
        word = word.lower()

        for a in word:
            ascii = ord(a) - 96
            asciivals.append(ascii)

        newword = ""
        for b in range(len(asciivals)):
            asciivals[b] += fibonacci(num-1)
            asciivals[b] = asciivals[b]%26
            num += 1
            if(asciivals[b] > 0 and asciivals[b] < 27):
                newword += chr(asciivals[b]+96)
            elif(asciivals[b] == 0):
                newword += "Z"
        newword = newword.upper()

        print(newword)

main()