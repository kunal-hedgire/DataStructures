'''
def Gen():
    First=1
    print("This will print first")
    yield First

    First += 1
    print("This will print Second")
    yield First

a=Gen()
next(a)
next(a)
next(a)
'''
'''
def Rev(mystr):
    length=len(mystr)
    for i in range(length -1,-1,-1):
        yield mystr[i]
for char in Rev("hello"):
 print(char)



#a=Rev("hello")
#list=a.__next__()
'''
'''
while True:
    try:
        list = a.__next__()
        print(list)

    except:
        break
'''
'''
def Pow(max=0):
    n=0
    while n < max:
        yield 2 ** n
        n += 1

a=Pow(10)
for b in a:
    print(b)
'''
#Infinity loop For Even Number Function
'''
def All_Even():

    n=0
    while True:
        yield n
        n +=2

a=All_Even()
for b in a:
    print(b)
'''