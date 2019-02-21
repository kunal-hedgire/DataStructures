class A:
    def __init__(self):
        self.x=10

    def myA(self):
        print('this is A class')

class B(A):
    def myA(self):
        print(self.x)
        print('this is a B  classs')

if __name__ == '__main__':
    b = B()
    a=A()
    a.myA()
    b.myA()

