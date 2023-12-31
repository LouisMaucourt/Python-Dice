import random
from rich import print
from dice import Dice
from character import Character, Mage, Warrior, Thief

def main():
    warrior = Warrior("Jojo", 20, 8, 3, 2, Dice(6))
    mage = Mage("Popy", 26, 6, 5, 4, Dice(6))
    thief = Thief("Marine", 15, 9, 10, 6, Dice(6))

    characters = [warrior, mage, thief]
    stats = {}

    car1 = random.choice(characters)
    characters.remove(car1)
    car2 = random.choice(characters)

    stats[car1.get_name()] = 0
    stats[car2.get_name()] = 0

    print(car1)
    print(car2)

    for i in range(100):
        car1.regenerate()
        car2.regenerate()
        while (car1.is_alive()) and (car2.is_alive()):
            car1.attack(car2)
            car2.attack(car1)
        if (car1.is_alive()):
            stats[car1.get_name()] += 1
        else:
            stats[car2.get_name()] += 1

    print(stats)

if __name__ == "__main__":
    main()
