def BinarySearch(A,x):
    if len(A)== 0 or (len(A)) == 1 and A[0] != x:
        return False

    mid = A[len(A)//2]
    if mid == x:
        return True
    if x < mid:
        return BinarySearch(A[:len(A)//2],x)
    if x > mid:
        return BinarySearch(A[len(A)//2+1:],x)

A=[10,20,30,40,50,55,88,99,100,110]
x=110#input('Enter number to be search:')
z=BinarySearch(A,x)
print(z)


