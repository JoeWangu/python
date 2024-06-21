#MODULE 2 WITH CLASSES AND MORE
#classes101
import random


def class101(): #remove def when running code. not supposed to be there only used to isolate code
    class Point:
        def move(self):
            print('move')     #pascal naming convention - classes don't use underscore instead capitalize every new word eg. Class EmailClient


        def draw(self):
            print('draw')

    #👆👆👆
    #create object from the class
    point1 =Point()
    point1.draw()
    point1.x = 10
    point1.y = 20
    print(point1.x)

    #another object
    point2 = Point()
    point1.move()
    point1.x = 10
    point1.y = 20


#constructors - functions that get called at the time of creating an object
def class102(): #remove def when running code. not supposed to be there only used to isolate code
    class PointA1:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y
        def move(self):
            print('move')     #pascal naming convention - classes don't use underscore instead capitalize every new word eg. Class EmailClient


        def draw(self):
            print('draw')

    #create object from the class
    point = PointA1(10,20)
    print(point.x, point.y)


def class103():
    class Person:
        def __init__(self,first_name,last_name) -> None:#constructor
            self.first_name = first_name
            self.last_name = last_name
        def talk(self):
            print(f'Hi I am {self.first_name} {self.last_name}')

    names = Person('John','Terry')
    #print(names.first_name,names.last_name)
    names.talk()
#create new object
    Bob = Person('Bob','Smith')
    #print(Bob.first_name,Bob.last_name)
    Bob.talk()


def inheritance101():
    class Animal:
        def walk(self):
            print('walk')


    class Dog(Animal):
        def bark(self):
            print('woof woof')

    class Cat(Animal):
        def be_annoying(self):
            print('meow everytime')
    

    dog1 = Dog()
    dog1.walk()
    dog1.bark()
    cat1 = Cat()
    cat1.be_annoying()
    

def randoms():
    members = ['john', 'mary','josh','lion','cookie']
    leader = random.choice(members)
    #print(leader)

    class Dice:
        def roll(self):
            i = random.randint(1,5)
            j = random.randint(1,5)
            return i,j


    dice = Dice()
    print(dice.roll())

