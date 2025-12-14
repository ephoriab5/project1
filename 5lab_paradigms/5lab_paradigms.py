from abc import ABC, abstractmethod
from random import randint

class Item(ABC):
    def __init__(self, name:str, health = 500):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self):
        pass

class Sword(Item): # Це наслідування
    def __init__(self, name, attack_power:int):
        super().__init__(name=name) #  Це виклик конструктора наслідуваного класу
        self.__attack_power = attack_power # приватний атрибут який реалізує інкапсуляцію
        self._sharp = 0
    
    def attack(self, another_item:Item): # ми не можемо створити клас без цього методу
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"Завдаємо удару мечем {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"
    
    @property
    def get_attack_power(self):
        return f"Атака меча {self.name}: {self.__attack_power + self._sharp} одиниць"
    
    def sharpening(self):
        self._sharp += 1

class Axe(Item): # Це наслідування
    def __init__(self, name, attack_power:int):
        super().__init__(name=name) #  Це виклик конструктора наслідуваного класу
        self.__attack_power = attack_power # приватний атрибут який реалізує інкапсуляцію
        self._sharp = 0
    
    def attack(self, another_item:Item):  # ми не можемо створити клас без цього методу
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return f"Завдаємо удару сокирою {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"

    @property
    def get_attack_power(self):
        return f"Атака сокири {self.name}: {self.__attack_power + self._sharp} одиниць"

class Bow(Item): # Це наслідування
    def __init__(self, name, attack_power:int):
        super().__init__(name=name) #  Це виклик конструктора наслідуваного класу
        self.__attack_power = attack_power # приватний атрибут який реалізує інкапсуляцію
    
    def attack(self, another_item:Item):  # ми не можемо створити клас без цього методу
        current_attack = self.__attack_power + randint(0, 15)
        another_item.health -= current_attack
        return f"Завдаємо удару луком {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"

    def reload(self, arrows:int):
        self.__attack_power += arrows
        return f"Лук {self.name} перезаряджено на {arrows} одиниць. Тепер атака становить {self.__attack_power} одиниць"
    
    @property
    def get_attack_power(self):
        return f"Атака лука {self.name}: {self.__attack_power} одиниць"
    
S = Sword("Ескалібур", 100)
A = Axe("Кратос", 95)
B = Bow("Лук", 80)

for i in range(10):
    print(f"Хід {i}")

    S.sharpening()
    print(S.attack(A))
    if S.health <= 0:
        print(f"Перемога за {A.name}")
        break

    print(A.attack(S))
    if A.health <= 0:
        print(f"Перемога за {S.name}")
        break
    
    print(B.attack(S))
    if B.health <= 0:
        print(f"Перемога за {S.name}")
        break