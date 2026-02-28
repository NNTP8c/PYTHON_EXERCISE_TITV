class Rectangle:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def compare(self, other):
        if self.area() > other.area():
            return f'{self.name} lớn hơn {other.name}'
        elif self.area() < other.area():
            return f'{self.name} nhỏ hơn {other.name}'
        else:
            return f'{self.name} bằng {other.name}'

rec1 = Rectangle(5, 10, 'rec1')
print("Diện tích rec1:", rec1.area()) 
print('Chu vi rec1:', rec1.perimeter())
rec2 = Rectangle(5, 10, 'rec2')
print(f'Diện tích rec2: {rec2.area()}')
print(f'Chu vi rec2: {rec2.perimeter()}')  
print(rec1.compare(rec2)) 
