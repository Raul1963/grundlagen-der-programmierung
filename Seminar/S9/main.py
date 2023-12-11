class Animal:
    def __init__(self, name):
        self.name=name

    def eat(self,w):
        print(f'{self.name} eating {w}')

class Pig(Animal):
    def __init__(self,name,age):
        Animal.__init__(self, name)
        self.age=age
    def sleep(self):
        print(f'{self.name} sleeping')

class Chicken(Animal):
    def __init__(self,name, color):
        Animal.__init__(self,name)
        self.color=color

class Farm:
    def __init__(self,name,city,animals=[]):
        self.name=name
        self.city=city
        self.animals=animals
    def feed_animals(self,food):
        for animal in self.animals:
            animal.eat(food)

def main():
    bob=Animal('bob')
    bob.eat('plante')
    zob=Pig('zob',2)
    zob.eat('ceva')
    zob.sleep()
    lob=Chicken('lob', 'black')
    lob.eat('iarba')

    f=Farm('ferma verde', 'cluj',[bob,zob,lob])
    f.feed_animals('plante')

main()