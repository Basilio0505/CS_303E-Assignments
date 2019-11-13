def bubbleSort(alist):
    count =-1
    while count != 0:
        count = 0
        for x in range(0,len(alist)-1):
            if alist[x] > alist[x+1]:
                temp = alist[x]
                alist[x] = alist[x+1]
                alist[x+1] = temp
                count += 1

def main():
    BigO = [189,154,111,99,76,45,44,2]
    LittleO = [2,34,56,62,89,107,143]
    Omega = [34,78,1,56,65,23,114,101]

    bubbleSort(BigO)
    bubbleSort(LittleO)
    bubbleSort(Omega)

    print(BigO)
    print(LittleO)
    print(Omega)

main()