import random

def Random_find_pivot(A,p,q):
    random_pivot_index  = random.randint(p,q)

    temp  = A[p]
    A[p] = A[random_pivot_index]
    A[random_pivot_index] = temp

    pivot = A[p]

    i = p
    for j in range(i+1,q+1,1):
        if A[j] < pivot:

            temp = A[i+1]
            A[i+1] = A[j]
            A[j] = temp


            i = i + 1

    temp  = A[i]
    A[i] = pivot
    pivot = temp

    A[p] = pivot

    return i



def Randomized_Quicksort(A,p,q):
    if p < q:
        r = Random_find_pivot(A,p,q)
        Randomized_Quicksort(A,p,r)
        Randomized_Quicksort(A,r+1,q)



if __name__ == '__main__':
    main()
#A = [6,10,13,5,8,3,2,11]
#print(A)
#Randomized_Quicksort(A,0,7)
#print(A)
