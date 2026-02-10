# n, m = [int(i) for i in input().split()]

# matrix = [[0] * m for _ in range(n)]
# num = 1


# while n and m:
#         for i in range(m):
#             matrix[0][i] = num
#             num += 1
#             if i == m - 1:
#                 m -= 1

#                 for j in range(1, n):
#                     matrix[j][m] = num
#                     num += 1
#                     if j == n - 1:
#                         n -= 1

#                         for k in range(m - 1, -1, -1):
#                             matrix[n][k] = num
#                             num += 1
#                             if k == 0:
#                                 m -= 1

#                                 for l in range(n - 1, 0):
#                                     matrix[l][k] = num
#                                     num += 1

#                                 n -= 1

# for row in matrix:
#     print(*row)

# lst = input().split()
# n = int(input())
# new_lst = []
# for l in range(n):
#     row = lst[l::n]
#     new_lst.append(row)

# print(new_lst)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]

# largest = matrix[n][n]

# for i in range(n):
#     for j in range(n):
#         if j + i + 1 >= n:
#             largest = max(largest, matrix[i][j])

# print(largest)


# n = int(input()
# s = 0
# matrix = [[int(i) for i in input().split()] for _ in range(n)]

# for i in range(s, n):
#     for j in range(s + 1, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     s += 1

# for row in matrix:
#     print(*row)

# n = int(input())

# snowflake = [['.'] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j + 1 == n or i == n // 2 or j == n // 2:
#             snowflake[i][j] = '*'

# for row in snowflake:
#     print(*row)

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]

# flag = 'YES'
# if n % 2 == 0:
#     for i in range(n // 2 + 1):
#         for j in range(n):
#             if i + j + 1 != n and matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
#                 flag = 'NO'
#                 break

# elif n % 2 == 1:
#     for i in range(n // 2):
#         for j in range(n):
#             if i + j + 1 != n and matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
#                 flag = 'NO'
#                 break

# print(flag)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]

# def latin_square(matrix, n):
#     for i in range(1, n):
#         if matrix[i][0] == matrix[i - 1][0]:
#             return 'NO'

#     for i in range(n):
#         numbers = [i for i in range(1, n + 1)]
#         for j in range(n):
#             if matrix[i][j] in numbers:
#                 numbers.remove(matrix[i][j])

#         if numbers:
#             return 'NO'

#     return 'YES'

# print(latin_square(matrix, n))

# coordinates = input()
# crd_x = '876543210'
# crd_y = 'abcdefgh'
# x = crd_x.index(coordinates[1])
# y = crd_y.index(coordinates[0])

# desk = [['.'] * 8 for _ in range(8)]

# for i in range(8):
#     for j in range(8):
#         if i == x or j == y or i - j == x - y or i + j == x + y:
#             desk[i][j] = '*'


# desk[x][y] = 'Q'

# for row in desk:
#     print(*row)


# n = int(input())
# matrix = [[0] * n for _ in range(n)]
# for i in range(n - 1):
#     num = 1
#     for j in range(i + 1, n):
#         matrix[i][j], matrix[j][i] = num, num
#         num += 1

# for row in matrix:
#     print(*row)
#
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# lst = []
# for tup in numbers:
#     avg = sum(tup) / len(tup)
#     lst.append(avg)
# print(lst)


# n, m, k, x, y, z = [int(input()) for _ in range(6)]
# total = z + n + m +k - x - y
# print(total)


# n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
# v = n + m - x
# r = m + k - y
# l = n + k - z
# only_n = n - l - v + t
# only_m = m - v - r + t
# only_k = k - l - r + t
# one_book = only_n + only_m + only_k
# print(one_book)
# two_book = v - t + r - t + l - t
# print(two_book)
# no_book = a - one_book - two_book - t
# print(no_book)


# n = input()
# uniq = set(n)
# if len(uniq) == len(n):
#     print('YES')
# else:
#     print('NO')


# n = set(input() + input())
# s = set(str(i) for i in range(10))
# print('YES' if n == s else 'NO')

# s = input().split()
# myset = [set(i) for i in s]
# print('YES' if myset[0] == myset[1] == myset[2] else 'NO')
# myset = ''
# for i in range(int(input())):
#     s = input().lower()
#     myset += s
# myset = set(myset)
# print(len(myset))

# s = {
#     ",",
#     ".",
#     ";",
#     ":",
#     "?",
#     "!",
#     "-",
# }
# txt = [i for i in input().lower() if i not in s]
# txt = ''.join(txt).split()
# uniq = set(txt)
# print(len(uniq))


# s = set()
# numbers = [int(i) for i in input().split()]
# for l in numbers:
#     if l in s:
#         print('YES')
#     else:
#         print('NO')
#         s.add(l)


# n = int(input())
# counter = 0
# myset = set()
# for _ in range(n):
#     stat = input().split(': ')
#     if stat[1] == 'Correct':
#         counter += 1
#         myset.add(stat[0])


# users = len(myset)
# if counter:
#     print(f'Верно решили {users} учащихся')
#     procent = int(counter / n * 100 + 0.5)
#     print(f'Из всех попыток {procent}% верных')
# else:
#     print('Вы можете стать первым, кто решит эту задачу')

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set1.difference(set2)
# print(*sorted(set3))

# n = int(input())
# myset = set(int(i) for i in input())
# for _ in range(n - 1):
#     s = (int(i) for i in input())
#     myset &= set(s)

# print(*sorted(myset))


# numbers = set(range(11))
# s1 = set(input().split())
# s2 = set(input().split())
# s3 = set(input().split())
# res = sorted((s1 | s2 | s3) ^ numbers, key=int)

# print(*res)


# myset = {png.lower() for png in files if png.lower().endswith('.png')}

# print(*sorted(myset))

# n, m, k, p = [int(input()) for _ in range(4)]

# print(n - (m + k - p))
# n = int(input())
# lst = [input() for _ in range(n)]
# myset = set(lst)
# repeater = -len(myset) + len(lst)
# if repeater > 0:
#     print('REPEAT')
# else:
#     print('OK')

# m, n = int(input()), int(input())

# library = {input() for _ in range(m)}

# for _ in range(n):
#     book = input()
#     if book in library:
#         print('YES')
#     else:
#         print('NO')

# one = set(input().split())
# two = set(input().split())
# res = one & two
# if res:
#     print(*sorted(res, reverse=True))
# else:
#     print('BAD DAY')


# set1 = {int(i) for i in input().split()}
# set2 = {int(i) for i in input().split()}
# print('YES' if set1 == set2 else 'NO')

# m, n = int(input()), int(input())

# mathem = {input() for _ in range(m)}
# info = {input() for _ in range(n)}
# only_one = mathem.symmetric_difference(info)
# if only_one:
#     print(len(only_one))
# else:
#     print('NO')

# set1 = {word for word in input().split()}
# set2 = {word for word in input().split()}
# print(*sorted(set1 | set2))

# m, n = int(input()), int(input())

# lst = [input() for _ in range(m + n)]
# myset = set(lst)
# if len(myset) == n == m:
#     print('NO')
# else:
#     print(len(myset) - (n + m - len(myset)))


# m = int(input())
# n = int(input())
# myset = {input() for _ in range(n)}
# for _ in range(m - 1):
#     n = int(input())
#     myset &= {input() for _ in range(n)}

# print(*sorted(myset), sep='\n')

# lst = []
# for row in users:
#     if 'email' in row and row['email']:
#         continue
#     lst.append(row['name'])
# print(*sorted(lst))


# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }

# n = input()
# str_n = (d[int(i)] for i in n)
# print(*str_n)


# d = {
#     ".": "1",
#     ",": "11",
#     "?": "111",
#     "!": "1111",
#     ":": "11111",
#     "A": "2",
#     "B": "22",
#     "C": "222",
#     "D": "3",
#     "E": "33",
#     "F": "333",
#     "G": "4",
#     "H": "44",
#     "I": "444",
#     "J": "5",
#     "K": "55",
#     "L": "555",
#     "M": "6",
#     "N": "66",
#     "O": "666",
#     "P": "7",
#     "Q": "77",
#     "R": "777",
#     "S": "7777",
#     "T": "8",
#     "U": "88",
#     "V": "888",
#     "W": "9",
#     "X": "99",
#     "Y": "999",
#     "Z": "9999",
#     " ": "0",
# }
# res = ''
# s = input().upper()
# for c in s:
#     if c in d:
#         res += d[c]

# print(res)

# morze = {
#     "A": ".-",
#     "B": "-...",
#     "C": "-.-.",
#     "D": "-..",
#     "E": ".",
#     "F": "..-.",
#     "G": "--.",
#     "H": "....",
#     "I": "..",
#     "J": ".---",
#     "K": "-.-",
#     "L": ".-..",
#     "M": "--",
#     "N": "-.",
#     "O": "---",
#     "P": ".--.",
#     "Q": "--.-",
#     "R": ".-.",
#     "S": "...",
#     "T": "-",
#     "U": "..-",
#     "V": "...-",
#     "W": ".--",
#     "X": "-..-",
#     "Y": "-.--",
#     "Z": "--..",
#     "0": "-----",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
# }
# s = input().upper()
# for c in s:
#     if c in morze:
#         print(morze[c], end=' ')

# text = 'bridge snake island game glory eye arrogant car nature game glory game'
# lst = text.split()
# mydict = {}
# for word in lst:
#     mydict[word] = mydict.get(word, 0) + 1
# max_v = 0
# min_k = lst[0]
# for k, v in mydict.items():
#     if max_v <= v:
#         max_v = v
#         min_k = min(min_k, k)
#         print(k)

# print(min_k)
# pets = [
#     ('Барсик', 'Маша', 'Петрова', 17),
#     ('Джек', 'Галина', 'Лагунова', 45),
#     ('Муся', 'Александр', 'Каракулов', 28),
#     ('Буся', 'Маша', 'Петрова', 17),
#     ('Кира', 'Вова', 'Пухарев', 54),
# ]
# mydict = {}
# for row in pets:
#     k = row[1:]
#     v = row[0]
#     mydict[k] = mydict.get(k, []) + [v]

# print(mydict)


# lst = [word.strip().lower() for word in input().split()]
# mydict = {}
# for word in lst:
#     mydict[word] = mydict.get(word, 0) + 1

# min_v = mydict[lst[0]]
# min_k = lst[0]

# for k, v in mydict.items():
#     if min_v > v:
#         min_v = v
#         min_k = k
#     elif min_v == v:
#         min_k = min(min_k, k)


# print(min_k)


# lst = input().split()
# dublicate = ''
# mydict = {}
# for i in lst:
#     if i in mydict:
#         n = mydict[i]
#         dublicate += f' {i}_{n}'
#     else:
#         mydict[i] = 0
#         dublicate += f' {i}'

#     mydict[i] += 1

# print(dublicate)


# n1 = int(input())
# mydict = {}
# for _ in range(n1):
#     s = input().split(': ')
#     k, v = s[0].lower(), s[1]
#     mydict[k] = v

# n2 = int(input())
# for _ in range(n2):
#     word = input().lower()
#     print(mydict.get(word, 'Не найдено'))


# s1 = [i.strip('.,!?:;-').lower() for i in input().split()]
# s2 = [i.strip('.,!?:;-').lower() for i in input().split()]
# d1 = {}
# d2 = {}
# for i in s1:
#     for j in i:
#         d1[j] = d1.get(j, 0) + 1

# for i in s2:
#     for j in i:
#         d2[j] = d2.get(j, 0) + 1

# print('YES' if d1 == d2 else 'NO')

# n = int(input())
# mydict = {}
# for _ in range(n):
#     s1, s2 = input().split()
#     mydict[s1] = s2
#     mydict[s2] = s1

# word = input()
# print(mydict[word])


# n1 = int(input())
# mydict = {}
# for _ in range(n1):
#     k, *v = input().split()
#     mydict[k] = v

# n2 = int(input())
# for _ in range(n2):
#     city = input()
#     for country in mydict:
#         if city in mydict[country]:
#             print(country)
#             break


# n1 = int(input())
# mydict = {}
# for _ in range(n1):
#     v, k = input().split()
#     mydict = mydict.setdefault(k.lower(), []).append(v)
#
# n2 = int(input())
# for _ in range(n2):
#     name = input().lower()
#     print(mydict.get(name, 'абонент не найден'))
#
#
# s = input()
# mydict = {}
# for i in s:
#     mydict[i] = mydict.get(i, 0) + 1
#
# for _ in range(int(input())):
#     k, v = input().split(': ')
#     for key in mydict:
#         if mydict[key] == v:
#             word = s.replace(key, k)
#
# print(s)
# s = '3:animal 4:house 8:tree 2:color 21:moon 31:fire 12:ship'
# res = {int(k): v for l in s.split() for k, v in [l.split(':')]}
# print(res)

# res = {
#     i: [j for j in range(1, i + 1) if i % j == 0]
#     for i in numbers
# }
# print(res)


# lst = [
#     {
#         id: {name: grade for name, grade in zip(student_names, student_grades)}
#         for id in student_ids
#     }
# ]
#
# print(lst)
# my_dict = {
#     'math_grades': [10, 7, 36, 14, 25], 'physics_grades': [14, 28, 7, 10, 36, 5],
#     'chemistry_grades': [10, 14, 19, 20, 21], 'geography_grades': [10, 15, 19, 34],
# }
# res = {}
# for i in my_dict:
#     res[i] = []
#     for j in my_dict[i]:
#         if j < 21:
#             res[i].append(j)
# print(res)

# res = []
# for domen in emails:
#     for user in emails[domen]:
#         adress = user + '@' + domen
#         res.append(adress)
#
# res.sort()
# print(*res, sep='\n')
#

# def DNA_to_RNA(DNA):
#     transfer = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
#     RNA = ''
#     for c in DNA:
#         RNA += transfer[c]
#     return RNA
#
# print(DNA_to_RNA(input()))
#
#
# print('Hello World')

# words = input().split()
# mydict = {}
# for word in words:
#     mydict[word] = mydict.get(word, 0) + 1
#     print(mydict[word], end=' ')

# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
#
# counter = 0
# word = input()
# for l in word:
#     for n in d:
#         if l in d[n]:
#             counter += n
#             break
#
# print(counter)
#
# def build_query_string(mydict):
#     s = ''
#     for key, value in sorted(mydict.items()):
#         s += f'{key}={value}&'
#
#     return s[:-1]


# def merge(values):
#     mydict = {}
#     for dct in values:
#         for k, v in dct.items():
#             mydict.setdefault(k, set()).add(v)
#
#     return mydict
# s = {'write': 'W', 'read': 'R','execute': 'X'}
# files = {}
# for _ in range(int(input())):
#     file, *permissions = input().split()
#     files[file] = permissions
#
# for _ in range(int(input())):
#     permission, file = input().split()
#     permission = s[permission]
#     if permission in files[file]:
#         print('OK')
#     else:
#         print('Access denied')

# mydict = {}
# for _ in range(int(input())):
#     name, goods, size = input().split()
#     if name not in mydict:
#         mydict[name] = {}
#     if  goods not in mydict[name]:
#         mydict[name].update({goods: 0})
#
#     mydict[name][goods] += int(size)
#
# for name, goods in mydict.items():
#     goods = dict(goods)
#     print(name + ':')
#     for l in goods.items():
#         print(*l)
#
# print(mydict.items())


# n = int(input())# количество попыток
# password = ''
# for _ in range(n):
#     password += chr((randint(65, 90), randint(97, 122))[randint(0, 1)])
#
# print(password)


# numbers = list()
# for _ in range(7):
#     number = randint(1, 49)
#     numbers.append(number)
# numbers.sort()
# print(*numbers)


# from random import randint
# def generate_ip():
#     ip = []
#     for _ in range(4):
#         num = randint(0, 255)
#         ip.append(str(num))
#
#     return '.'.join(ip)
#
#
# print(generate_ip())


# from random import choice as ch
# import string
# def generate_index():
#     letters = string.ascii_uppercase
#     digits = string.digits
#     return f'{ch(letters)}{ch(letters)}{ch(digits)}{ch(digits)}_{ch(digits)}{ch(digits)}{ch(letters)}{ch(letters)}'
#
#
# print(generate_index())


# from random import randint as r
# s = set()
# while len(s) < 100:
#     ticker = r(1_000_000, 9_999_999)
#     if ticker in s:
#         continue
#     s.add(ticker)
#     print(ticker)


# from random import randint, sample as s
#
#
# numbers = s(range(1, 76), 25)
# bingo = [[0] * 5 for i in range(5)]
# counter = 0
# for i in range(5):
#     for j in range(5):
#         bingo[i][j] = str(numbers[counter]).ljust(3)
#         counter += 1
#
# bingo[2][2] = '0'.ljust(3)
# for row in bingo:
#     print(*row)

# from random import randrange as r
#
# lst = []
# for _ in range(int(input())):
#     lst.append(input())
#
# friends = lst.copy()
# friend = friends[r(len(friends))]
# for name in lst:
#     while friend == name:
#         friend = friends[r(len(friends))]
#
#     print(name, '-', friend)
#     friends.remove(friend)
#     if friends:  # Проверка, что список не пустой
#         friend = friends[r(len(friends))]


# from string import *  # noqa: F403
# from random import sample as s

# LETTER = "".join((set(ascii_letters) | set(digits)) - set("lI1oO0"))  # noqa: F405
# uppers = "ABCDEFGHJKLMNPQRSTUVWXYZ"       # noqa: F405
# lowers = "abcdefghijkmnpqrstuvwxyz"  # noqa: F405
# digits = "23456789" # noqa: F405

# def generate_password(length):
#     password = []
#     password.append(s(uppers, 1)[0])
#     password.append(s(lowers, 1)[0])
#     password.append(s(digits, 1)[0])
#     password += s(LETTER, length - 3)
#     return ''.join(s(password, length))
    


# def generate_passwords(count, length):
#     lst = []
#     for _ in range(count):
#         lst.append(generate_password(length))
#     return lst


# n, m = int(input()), int(input())
# passwords = generate_passwords(n, m)

# print(*passwords, sep="\n")

# from decimal import * 
# num = Decimal(input())
# n = -(num.as_tuple().exponent)
# n = str(num)[-10:]
# print(Decimal(min(n)) + Decimal(max(n)))

import turtle

speed = 5
def move_up():                             # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x, y + speed)
  
def move_down():                           # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x, y - speed)

def move_left():                           # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x - speed, y)

def move_right():                          # функция обратного вызова
  x, y = turtle.pos()
  turtle.setposition(x + speed, y)
  
def change():                              # функция обратного вызова
  if turtle.isvisible():
    turtle.up()
    turtle.hideturtle()
  else:
    turtle.down()
    turtle.showturtle()
    
def speed_increase():                      # функция обратного вызова
  global speed
  speed += 1

def speed_decrease():                      # функция обратного вызова
  global speed
  speed -= 1

turtle.showturtle()                        # отображаем черепашку
turtle.pensize(3)                          # устанавливаем размер пера
turtle.Screen().listen()                   # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')       # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')   # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')   # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right') # регистрируем функцию на нажатие клавиши направо
turtle.Screen().onkey(change, 'space')
turtle.Screen().onkey(speed_increase, 'q')
turtle.Screen().onkey(speed_decrease, 'w')  






























