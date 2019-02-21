
class Dog:
    def bark(self):
        print('dog barking')

    def Friend(self):
        print('mans friends')

class Cat(Dog):
    def Meua(self):
        print('Cat meau')

class Tiger(Cat):
    def roar(self):
        print('Tiger Roar')

    def Friend(self):
        super().Friend()
        print('King of Jungle')


if __name__ == '__main__':
    t=Tiger()
    t.bark()
    t.Friend()
    t.Meua()
    t.roar()