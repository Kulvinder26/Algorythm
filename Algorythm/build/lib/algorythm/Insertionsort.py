import math

def Insertionsort(A):
    for i in range(len(A)):
        value = A[i]
        key = i
        j = i-1
        while(j >= 0 and A[j] > value):
            A[j+1] = A[j]
            j-=1
        A[j+1] = value


if __name__ == '__main__':
    main()


#A = [6,10,13,5,8,3,2,11]

#print(A)
#Insertionsort(A)
#print(A)
