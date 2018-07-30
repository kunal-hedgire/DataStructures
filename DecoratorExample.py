'''
def Pretty(func):
    def inner():
        print("I got Decorator")
        func()
    return inner

def Ordinary():
    print("I am ordinary ")



my= Pretty(Ordinary)
my()
'''
'''
def Pretty(func):
    def inner():
        print("I got Decorator")
        func()
    return inner
@Pretty
def Ordinary():
    print("I am ordinary ")


#Ordinary()
pr = Pretty(Ordinary)
pr()
'''
'''

def Divide(func):
    def inner(a,b):
        print('I am going divide:--' +str(a)+'--and--'+str(b))
        if b == 0 :
            print("Cant divide by zero")
            return
        return func(a,b)
    return inner



@Divide
def Sdivide(a,b):
    return a/b

#Divide(Sdivide(10,0))
print(Sdivide(1000,10))
'''

def func3(func):
    print("*>" *20)
    func()

def func2(func):
    print("*<" * 20)
    func()
    return


@func2
@func3
def func1():
        print('Hello')










