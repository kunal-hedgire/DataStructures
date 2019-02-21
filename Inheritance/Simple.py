import filecmp
class A:
    def fun(self):
        self.name='kunal'

class B(A):
    def fun1(self):
        self.age=25
        print('age=',self.age,'name=',self.name)

if __name__ == '__main__':
    b=B()
    b.fun()
    b.fun1()
    print(b.name,b.age)

    print(help(filecmp))