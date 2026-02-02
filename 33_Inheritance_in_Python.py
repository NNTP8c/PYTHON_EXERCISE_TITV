#
# Created on Sun Feb 01 2026
#
# Copyright (c) 2026 Your Company
#
# Lessin 33: Inheritance - Kế thừa

class animal():
    def __init__(self, typeAnimalA, nameA, heightA, widthA, weightA):
        self.typeAnimal = typeAnimalA
        self.name = nameA
        self.height = heightA
        self.width = widthA
        self.weight = weightA
    def makeSound(self):
        print('Unknow')
    def printMe(self):
        print('Name: {0}, Height: {1}, Width: {2}, Weight: {3}'.format(self.name, self.height, self.width, self.weight))
people = animal('Người', 'Thành', '170cm', '80cm', '60kg')
people.printMe()

class dog(animal):
    def __init__(self, nameA, heightA, widthA, weightA, isChampionA):
        animal.__init__(self, 'Dog', nameA, heightA, widthA, weightA)
        self.ischampion = isChampionA
    def makeSound(self):
        print('{0}: gau gau'.format(self.name))
dog1 = dog('Vàng', '40cm', '15cm', '25kg', 'Chạy nhanh')
dog1.makeSound()
dog1.printMe()

class cat(animal):
    def __init__(self, nameA, heightA, widthA, weightA, colorA):
        animal.__init__(self, 'Cat', nameA, heightA, widthA, weightA)
        self.color = colorA
    def makeSound(self):
        print('{0}: meow meow'.format(self.name))
cat1 = cat('Tom', '90cm', '20cm', '30kg', 'xanh')
cat1.printMe()