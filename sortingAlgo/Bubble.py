'''
def bubble(A):
    for i in range(0,len(A)):
        for k in range(len(A)-1,i,-1):
            if (A[k] < A[k-1]):
                swap(A,k,k-1)

def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp

A=[566,45,789,100,900,150,40,10,5,68,69]
bubble(A)
print(A)
'''
#second way to perform bubble sort

def bubble(A):
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

a=[566,45,789,100,900,150,40,10,5,68,69]
bubble(a)
print('second way',a)

