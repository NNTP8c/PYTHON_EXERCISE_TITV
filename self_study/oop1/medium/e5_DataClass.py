from dataclasses import dataclass
@dataclass
class Poduct:
    name: str
    price: float
    quantity: int

    def price_total(self):
        return self.price * self.quantity
    
pro = Poduct('Cây quạt', 123.4, 2)

print(pro.price_total())