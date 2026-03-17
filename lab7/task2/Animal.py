class animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def make_sound(self):
        return "makes some kind of sound"
    
    def into(self):
        return f"{self.name} - this {self.breed}, to him {self.age} age." 
    
    def __str__(self):
        return f"Объект Animal: {self.name}"