#Basilio Bazan
#bb36366
def quick_sort(A):
    quick_sort2(A,0,len(A)-1)

def quick_sort2(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort2(A, low, p-1)
        quick_sort2(A, p+1, high)

def get_pivot(A, low, high):
    mid = (high + low) //2
    pivot = high
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            pivot = mid
    elif A[low] < A[high]:
        pivot = low
    return pivot

def partition(A, low, high):
    pivotIndex = get_pivot(A, low, high)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low

    for i in range(low, high+1):
        if A[i] < pivotValue:
            border +=1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return (border)

def main():
    file = open("input.txt", "r")
    list1 = []
    for i in file:
        list1.append(i.strip("\n").title())

    quick_sort(list1)
    for x in list1:
        print(x)

main()