# def next_bigger(n):
#     num = list(str(n))

#     for i in range(len(num) - 1, 0, -1):
#         j = i - 1
#         if num[j] < num[i]:
#                 min_idx = min(
#                 (idx for idx in range(i, len(num)) if num[idx] > num[j]),
#                 key=lambda idx: num[idx]
#                 )

#                 num[j], num[min_idx] = num[min_idx], num[j]
#                 num = num[:i] + num[i:][::-1]
#                 return int(''.join(num))
    
#     return -1
            
            
# print(next_bigger(59884848459853))  

# size_x, size_y = map(int, input().split())


# def turn(vector: list) -> list:
#     return [vector[1], -vector[0]]


# def next_step(row: int, column: int, vector: list, matrix: list) -> tuple:
#     next_row = row + vector[0]
#     next_column = column + vector[1]

#     if not (0 <= next_row < size_x and 0 <= next_column < size_y and matrix[next_row][next_column] == 0):
#         vector = turn(vector)
#         next_row = row + vector[0]
#         next_column = column + vector[1]

#     return next_row, next_column, vector


# matrix = [[0] * size_y for _ in range(size_x)]

# row, column = 0, 0
# vector = [0, 1]

# for number in range(1, size_x * size_y + 1):
#     matrix[row][column] = number
#     if number < size_x * size_y:
#         row, column, vector = next_step(row, column, vector, matrix)

# max_width = len(str(size_x * size_y))

# for row in matrix:
#     print(*(f"{number:>{max_width}}" for number in row))


# class Example:
#     def __init__(self, value):
#         self.set_value(value)

#     def set_value(self, new_value):
#         if isinstance(new_value, int) and new_value >= 0:
#             self.value = new_value


# example = Example(-1)
# print(example.value)  # Output: 5

# class StringSource:
#     def __init__(self, s):
#         self.s = s
#     def get_length(self):
#         return len(self.s)

# class ListSource:
#     def __init__(self, lst):
#         self.lst = lst
#     def get_length(self):
#         return len(self.lst)

# def print_source_length(source):
#     print(f"Длина источника: {source.get_length()}")

class Character:
    def __init__(self, name, damage):
        self.name = name
        self._health = 100
        self._damage = damage 
        
    def attack(self, target):
        if hasattr(target, 'take_damage') and callable(target.take_damage):
            target.take_damage(self._damage)   
         
    def take_damage(self, amount):
         self._health -= amount
         
    def get_status(self):
        return f"Имя: {self.name}, Здоровье: {self._health}"


class Warrior(Character):
    def __init__(self, name, damage, armor):
        super().__init__(name, damage)
        self.armor = armor 
    
    def take_damage(self, amount):
        damage = amount - self.armor
        if damage > 0:
            self._health = damage
            
class Mage(Character):
    def __init__(self, name, damage, mana):
        super().__init__(name, damage)
        self.mana = mana 

    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            super().attack(self, target)

# Создаем персонажей
warrior = Warrior("Конан", 15, 5) # Урон 15, Броня 5
mage = Mage("Раистлин", 20, 100) # Урон 20, Мана 100

print(warrior.get_status())
print(mage.get_status())
print("--- Битва ---")

# Маг атакует воина
mage.attack(warrior)
print(warrior.get_status()) # Воин должен получить 15 урона (20 - 5 брони)

# Воин атакует мага
warrior.attack(mage)
print(mage.get_status()) # Маг должен получить 15 урона

# Проверка логики мага
mage.mana = 5 # Устанавливаем мало маны
mage.attack(warrior)
print(warrior.get_status()) # Здоровье воина не должно измениться





















