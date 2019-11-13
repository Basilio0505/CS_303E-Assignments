def selectSort(alist):
    for x in range(0,len(alist)):
        temp = alist[x]
        for y in range(x,len(alist)):
            if temp > alist[y]:
                temp = alist[y]
                alist[y] = alist[x]
                alist[x] = temp

def main():
    mylist = [24,6,54,45,67,82,10]
    selectSort(mylist)
    print(mylist)

main()