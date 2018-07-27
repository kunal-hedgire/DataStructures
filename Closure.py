'''
count=0
print("Count",count)#0
def Hi():
    global count
    count=10
    print(" inside Hi ",count)#10

    def Bye():

        #nonlocal count
        #count = 20
        print("inside Bye",count)#10
    Bye()
    print('Inside Hi',count)#10
Hi()
print('Global',count)#10
'''
def multiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier
times3=multiplier_of(5)
times4=multiplier_of(10)
print(times3(9))
print(times4(5))






