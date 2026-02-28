class CPU:
    def __init__(self, name):
        self.name = name
    def get_cpu(self):
        return f'Tên CPU: {self.name}'
    
class RAM:
    def __init__(self, size):
        self.size = size
    def get_ram(self):
        return f'Kích thước RAM: {self.size}'

class Computer:
    def __init__(self, cpu: CPU, ram: RAM):
        self.cpu = cpu
        self.ram = ram
    def get_cpu(self):
        return self.cpu.get_cpu()
    def get_ram(self):
        return self.ram.get_ram()



print(Computer(CPU('a'), RAM(8)).get_ram())
print(Computer(CPU('a'), RAM(8)).get_cpu())