import sys
class RegularClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class SlotsClass:
    __slots__ = ['a', 'b', 'c'] 
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

regular = [RegularClass(1,2,3) for _ in range(1000)]
regular_size = sum(sys.getsizeof(obj) for obj in regular)

slots = [SlotsClass(1,2,3) for _ in range(1000)]
slot_size = sum(sys.getsizeof(obj) for obj in slots)
print(f'Dung lượng bộ nhớ regular sử dụng: {regular_size}')
print(f'Dung lượng bộ nhớ slots sử dụng: {slot_size}')