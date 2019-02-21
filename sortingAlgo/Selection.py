def seelction(A):
    for i in range(len(A)):
        least = i
        for k in range(i+1,len(A)):
            if A[k] < A[least]:
                least = k
        swap(A,least,i)
        return A

def swap(A,x,y):
    A[x],A[y]=A[y],A[x]


a=[500,10,5,80,40,35,10,20,25,502,24]
print(seelction(a))
