from Animal import animal

class Dog(animal):
    def __init__(self, name, breed, age, size):
        super().__init__(name, breed, age)
        self.size = size

    def make_sound(self):
        return "Woof-woof"
    
    def run(self):
        return f"{self.name} run fast!"
    