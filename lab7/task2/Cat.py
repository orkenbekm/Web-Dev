from Animal import animal

class Cat(animal):
    def __init__(self, name, breed, age, food):
        super().__init__(name, breed, age)
        self.food = food

    def make_sound(self):
        return "Meow-meow!"
    
    def hunt(self):
        return f"{self.name} hunt for mouse."