
from Dog import Dog
from Cat import Cat

def main():
 
    my_dog = Dog(name="Нурасыл", breed="Овчарка", age=4, size="Большой")
    
    my_cat = Cat(name="Ахмет", breed="Сиамская", age=2, food="Рыба")

    animals_list = [my_dog, my_cat]

    print("Tests")

    for animal in animals_list:
        print("--------------------")

        print(f"Объект: {animal}") 
        
        print(f"Инфо: {animal.into()}") 
        
        print(f"Голос: {animal.make_sound()}")

    print("----------------------")

    print("\nChallenging Children's Unique Methods")
    
    print(my_dog.run())

    print(f"Dogs size: {my_dog.size}")
    
    print(my_cat.hunt())

    print(f"cats fivorite food: {my_cat.food}")

if __name__ == "__main__":
    main()