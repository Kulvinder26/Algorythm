import math
import random


def Max_heapify(A,i):
    l = i*2+1
    r = 2*i+2
    large = i

    if(l<heapsize):
        if(A[l] > A[i]):
            large = l
        else:
            large = i
    if(r<heapsize):
       if(A[large] < A[r]):
           large = r
    if(large != i):
        temp = A[i]
        A[i] = A[large]
        A[large] = temp
        Max_heapify(A,large)


def Build_Max_heap(A):
    length = len(A)
    for i in range(math.floor(length/2)-1,-1,-1):
        Max_heapify(A,i)

def Heapsort(A):
    Build_Max_heap(A)
    length = len(A)
    global heapsize
    for i in range(length-1,0,-1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        heapsize = heapsize - 1
        Max_heapify(A,0)


if __name__ == '__main__':
    main()

#A = [ random.randint(-1000,1000) for k in range(0,200)]
#random.shuffle(A)
#A = [2, 14, 1, 8, 71, 92, 31, 163, 42, 20]
#heapsize =  len(A)
#print(A)
#Heapsort(A)
#print(A)
