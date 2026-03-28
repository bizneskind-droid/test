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


# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     return [[value] * m for _ in range(n)]

# print(matrix())         # матрица 1 × 1 из 0
# print(matrix(3))        # матрица 3 × 3 из 0
# print(matrix(2, 5))     # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))  # матрица 3 × 4 из 9

# def sq_sum(*args):
#     return sum(i ** 2 for i in args)


# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def mean(*args):
#    numbers = [i for i in args if type(i) is float or type(i) is int]
#    if len(numbers) == 0:
#        return 0
#    avg = sum(numbers) / len(numbers)
#    return avg


# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def greet(name, *args):
#     args =  (name,) + args
#     return f'Hello, {' and '.join(args)}!'


# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))


# def print_products(*args):
#     products = [product for product in args if type(product) is str and product.isalpha()]
#     if products:
#         mydict = {f'{i + 1})': products[i] for i in range(len(products))}
#         for item in mydict.items():
#             print(*item)
#     else:
#         print('Нет продуктов')
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


# m = {1: 'one', 2: 'two', 3: 'three'}
# lst = sorted(m.items(), key=lambda x: x[1])
# print(lst)


# def start():
#     # тело функции start
#     print('start')


# def stop():
#     # тело функции stop
#     print('stop')


# def pause():
#     # тело функции pause
#     print('pause')


# commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция

# command = input()  # считываем название команды

# commands[command]()  # вызываем нужную функцию через словарь по ключу


# сортируем по сумме кортежа


# def generator_square_polynom(a, b, c):
#     def square_polynom(x):
#         return a * x**2 + b * x + c

#     return square_polynom


# f = generator_square_polynom(a=1, b=2, c=1)
# g = generator_square_polynom(a=2, b=0, c=-3)
# h = generator_square_polynom(a=-3, b=-10, c=50)

# print(f(1))
# print(g(2))
# print(h(-1))
# print(f.__closure__)


# lst = ('12 14 79 7 4 123 45 90 111').split()

# print(*sorted(lst, key=lambda x: (sum[int(i) for i in x], int(x)))

# def generation_variants(n, m=None, prefix=None, used=None):
#     m = m if m is not None else n

#     if m == 0:
#         print(*prefix)
#         return

#     prefix = prefix or []
#     used = used or [False for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         if used[i]:
#             continue

#         prefix.append(i)
#         used[i] = True

#         generation_variants(n, m-1, prefix, used)

#         prefix.pop()
#         used[i] = False


# generation_variants(4)

# def merge(lst1, lst2):
#     a, b = 0, 0
#     len1, len2 = len(lst1), len(lst2)
#     lst = []

#     while a < len1 and b < len2:
#         if lst1[a] <= lst2[b]:
#             lst.append(lst1[a])
#             a += 1
#         else:
#             lst.append(lst2[b])
#             b += 1


#     lst += lst1[a:]
#     lst += lst2[b:]

#     return lst

# def merge_sort(lst):
#     if len(lst) <= 1:
#         return

#     middle = len(lst) // 2

#     left = lst[:middle]
#     right = lst[middle:]

#     merge_sort(left)
#     merge_sort(right)

#     res = merge(left, right)

#     for i in range(len(lst)):
#         lst[i] = res[i]


# tests()


# def NOD(a, b):
#     if b == 0:
#         return a

#     return NOD(b, a % b)


# print(NOD(18, 48))
# def tests():
#     a = [1, 3, 4, 6, 3, 4, 3, 1, 0, 432]
#     hoana_sort(a)
#     print(*a)

#     a = [7, 7, 8, 9, -1, 34, 4, 8]
#     hoana_sort(a)
#     print(*a)


# def hoana_sort(lst):
#     if len(lst) <= 1:
#         return

#     barrier = lst[0]
#     left, middle, right = [], [], []

#     for x in lst:
#         if x < barrier:
#             left.append(x)
#         elif x == barrier:
#             middle.append(x)
#         else:
#             right.append(x)

#     hoana_sort(left)
#     hoana_sort(right)

#     res = left + middle + right
#     for i in range(len(res)):
#         lst[i] = res[i]


# tests()

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result

# def round(number):
#     return f'{number:.2f}'


# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

# print(*map(round, numbers), sep='\n')


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result

# def func(num):
#     if 99 < num < 1000 and num % 5 == 2:
#         return num

# def func1(num):
#     return num**3


# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

# print(*map(func1, filter(func, numbers)), sep='\n')


# def increase(num):
#     return num + 7


# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = sum(map(increase, numbers))

# print(new_numbers)

# def generator_square_polynom(a, b, c):
#     return lambda x: a*x**2 + b*x + c

# a = generator_square_polynom(1, 3, 4)

# print(a)

# from functools import reduce

# data = [
#     ["Tokyo", 35676000, "primary"],
#     ["New York", 19354922, "nan"],
#     ["Mexico City", 19028000, "primary"],
#     ["Mumbai", 18978000, "admin"],
#     ["Sao Paulo", 18845000, "admin"],
#     ["Delhi", 15926000, "admin"],
#     ["Shanghai", 14987000, "admin"],
#     ["Kolkata", 14787000, "admin"],
#     ["Los Angeles", 12815475, "nan"],
#     ["Dhaka", 12797394, "primary"],
#     ["Buenos Aires", 12795000, "primary"],
#     ["Karachi", 12130000, "admin"],
#     ["Cairo", 11893000, "primary"],
#     ["Rio de Janeiro", 11748000, "admin"],
#     ["Osaka", 11294000, "admin"],
#     ["Beijing", 11106000, "primary"],
#     ["Manila", 11100000, "primary"],
#     ["Moscow", 10452000, "primary"],
#     ["Istanbul", 10061000, "admin"],
#     ["Paris", 9904000, "primary"],
# ]

# big_cities = filter(lambda x: x[1] > 10_000_000 and x[2] == 'primary', data)

# name_cities = sorted(map(lambda x: x[0], big_cities))

# result = 'Cities: ' + reduce(lambda x, y: x + ', ' + y, name_cities)

# print(result)

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

# print(*map(lambda n: n // 2 if n % 2 == 0 else n, filter(lambda n: n < 48, numbers)))


# data = [
#     (19542209, "New York"),
#     (4887871, "Alabama"),
#     (1420491, "Hawaii"),
#     (626299, "Vermont"),
#     (1805832, "West Virginia"),
#     (39865590, "California"),
#     (11799448, "Ohio"),
#     (10711908, "Georgia"),
#     (10077331, "Michigan"),
#     (10439388, "Virginia"),
#     (7705281, "Washington"),
#     (7151502, "Arizona"),
#     (7029917, "Massachusetts"),
#     (6910840, "Tennessee"),
# ]

# data.sort(key=lambda item: item[1][-1], reverse=True)

# for population, state in data:
#     print(f'{state}: {population}')


# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

# print(max(mixed_list, key=lambda x: (type(x) is int, x)))


# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]


# print(*sorted(mixed_list, key=lambda x: (type(int), t


# def left_bound(lst, value):
#     left = -1
#     right = len(lst)

#     while right - left > 1:
#         middle = (left + right) // 2
#         if lst[middle] < value:
#             left = middle
#         else:
#             right = middle
            
#     return left

# def right_bound(lst, value):
#     left = -1
#     right = len(lst)

#     while right - left > 1:
#         middle = (left + right) // 2
#         if lst[middle] <= value:
#             left = middle
#         else:
#             right = middle
            
#     return right

# # ...existing code...

# lst = [1, 2, 2, 2, 3, 5]
# value = 2

# l = left_bound(lst, value)   # 0 (последний элемент < 2 на позиции 0)
# r = right_bound(lst, value)  # 4 (первый элемент > 2 на позиции 4)
# count = r - l - 1             # 3 (три двойки в списке)

# print(f"Левая граница: {l}, Правая граница: {r}, Количество: {count}")
# # Вывод: Левая граница: 0, Правая граница: 4, Количество: 3



# abscissas = list(map(float, input().split()))
# ordinates = list(map(float, input().split()))
# applicates = list(map(float, input().split()))
# points = zip(abscissas, ordinates, applicates)  

# print(all(map(lambda x, y, z: x**2 + y**2 + z**2 >4, abscissas, ordinates, applicates)))


# start = int(input())
# end = int(input())
# lst =list(range(start, end + 1))
# lst = filter(lambda x: '0' not in str(x) and all(x % int(num) == 0 for num in str(x)), lst)

# print(*lst)


# def calculate_min_cost(n: int, price: list):
#     k = [0] * (n + 1)
#     k[0] = float('-inf')
#     k[1] = price[1]
#     k[2] = k[1] + price[2]
#     k[3] = min(k[1], k[2]) + price[3]
    
    
#     for i in range(4, n + 1):
#         if i % 3 == 0:
#             k[i] = min(k[i - 1], k[i - 2], k[i // 3]) + price[i]
#         else:
#              k[i] = min(k[i - 1], k[i - 2]) + price[i]
             
#     path = []
             
#     for i in range(n, 1, -1):
#         if i % 3 == 0:
#             prev = min(
    
    
    
    
    
#     return k[n]
    
    
    
# print(calculate_min_cost(9, [0, 2, 2, 10, 4, 5, 20, 7, 8, 9]))



# password = input()
# if len(password) > 6:
#     low = any(map(lambda ch: ch.islower(), password))
#     high = any(map(lambda ch: ch.isupper(), password))
#     digit = any(map(lambda ch: ch.isdigit(), password))

# print(['NO', 'YES'][int(all([low, high, digit]))])



# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f'''
# To: {mail} \n
# Приветствую, {name}!  \n
# Вам назначен экзамен, который пройдет {date}, в {time}. \n
# По адресу: {place}.  \n
# Экзамен будет проводить {teacher} в кабинете {number}. \n
# Желаем удачи на экзамене!
# '''
    
    
            

# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))


# def concat(*args, sep=' '):
#     if len(args) <= 1:
#         return ''.join(args)
#     res = ''
#     for i, arg in enumerate(args):
#         res += str(arg) + sep
#         if i == len(args) - 2:
#             res += str(args[i + 1])
#             return res
    



# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))



# from random import choice as ch

# file = open('/home/almaz/lines.txt', 'r')   # по умолчанию режим доступа для чтения ('r')

# print(ch(file.readlines()))

# file.close()



# def move_zeros(array):
#     for i in array:
#         if i == 0:
#             array.remove(i) # Remove the element from the array
#             array.append(i) # Append the element to the end
#     return array



# print(move_zeros([0, 1, 0, 0]))



# with open('lines.txt') as file:
#     largest = max(file.readlines(), key=len)
#     print(largest.strip())

#     file.seek(0)
#     flag = False

#     for line in file:
#         if flag and len(line) == len(largest):
#             print(line.strip())
            
#         elif line == largest:
#             flag = True


# with open('nums.txt') as file:
#     total = 0
#     for line in file:
#         for row in line.split():
#             if row.isdigit():
#                 total += int(row)
#                 continue
            
#             num = ''
#             flag = False
  
#             for i in range(len(row)):
#                 if row[i].isdigit():
#                     flag = True
#                     num += row[i]
#                     continue
                    
#                 if flag:
#                     total += int(num)
#                     num = ''
#                     flag = False
                    
#             if flag:
#                 total += int(num)
#                 num = ''
#                 flag = False
            
            
# print(total)               




# with open('file.txt', encoding='utf-8') as file:
#     lines = 0
#     words = 0
#     chars = 0

#     for lines, row in enumerate(file, 1):
#         words += len(row.split())
#         chars += sum(ch.isalpha() for ch in row)

# print(f"""Input file contains:
# {chars} letters
# {words} words
# {lines} lines""")
        
        
# from random import choice as ch
       
    
# with open('first_names.txt') as names, open('last_names.txt') as surnames:
#     names, surnames = list(names), list(surnames)
#     for _ in range(3):
#         name = ch(names).strip()
#         surname = ch(surnames).strip()
#         print(f'{name} {surname}')
    
    
# with open('population.txt') as file:
#     for line in file:
#         city, population = line.split('\t')
        
#         if city.startswith('G') and int(population) > 500_000:
#             print(city)
    
    
# def read_csv():
#     lst = []
#     with open('data.csv') as file:
#         keys = file.readline().strip().split(',')
#         for line in file:
#             values = line.strip().split(',')
#             info = {key: value for key, value in zip(keys, values)}
            
#             lst.append(info)
            
#         return lst
    
# print(read_csv())
    
    
    
    
    
# with open('goats.txt') as goats, open('answer.txt', 'w') as answer:
#     goats.readline()
    
#     colours = {}
#     for counter, line in enumerate(goats):
#         if line.strip() == 'GOATS':
#             continue
#         colour = line.strip().split()[0]
#         colours[colour] = colours.get(colour, -1) + 1
    
#     verify = (counter - len(colours)) * 0.07
#     for colour, т in sorted(colours.items()):
#         if counter >= verify:
#             print(f'{colour} goat', end='\n', file=answer)
        

# with open('words.txt') as words:
#     largests = []
#     max_len = 0
#     word = ''
#     for line in words:
#         for ch in line:
#             if ch != ' ' and ch != '\n':
#                 word += ch
#                 continue
#             if len(word) > max_len:
#                 max_len = len(word)
#                 largests = [word]
#             elif len(word) == max_len:
#                 largests.append(word)
                
#             word = ''
            
            
# with open('words.txt') as words:
#     largests = []
#     max_len = 0

#     for line in words:
#         for word in line.rstrip().split():
#             if len(word) > max_len:
#                 max_len = len(word)
#                 largests = [word]
#             elif len(word) == max_len:
#                 largests.append(word)
            
# with open('forbidden_words.txt') as forb, open('data3.txt', 'r') as inp:
#     forb = forb.read().split()
#     s = inp.read()
#     s_lower = s.lower()
#     for word in forb:
#         s_lower = s_lower.replace(word, '*' * len(word))
    
#     res = ''.join(s[i] if s_lower[i] != '*' else '*' for i in range(len(s)))
    
#     with open('data3.txt', 'w') as out:
#         out.write(res)

#     print(res)
     
        


# with open('transliteration.txt', 'w') as out, open('cyrillic.txt') as inp:
#     d = {
#     'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
#     }
#     for s in inp.read():
#         res = d.get(s.lower(), s)
#         out.write(res if s.islower() else res.capitalize())


# with open('data3.txt') as file:
#     flag = False
#     lst = []
#     for line in file:
#         if 'def ' in line and flag is False:
#             start = line.find(' ') + 1
#             end = line.find('(')
#             name = line[start: end]
#             lst.append(name)
            
#         elif '#' in line:
#             flag = True
            
#         elif 'def ' in line and flag:
#             flag = False
            
# print(*lst, sep='\n')
            
            
# def lcs(a, b):
#     n, m = len(a) + 1, len(b) + 1
    
#     dp = [[0] * m for _ in range(n)]
    
#     for i in range(1, n):
#         for j in range(1, m):
#             if a[i - 1] == b[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j  - 1]) 
                
#     res = []
    
#     i, j = n - 1, m - 1
#     while i > 0 and j > 0:
#         if a[i - 1] == b[j - 1]:
#             res.append(a[i - 1])
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] >= dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1
            
                
#     return dp[-1][-1], res[::-1]
               
# def lis(a):
#     dp = [1] * len(a)
#     prev = [-1] * len(a)
#     for i in range(1, len(a)):
#         for j in range(i):
#             if a[j] < a[i] and dp[j] + 1 > dp[i]:
#                 dp[i] = dp[j] + 1
#                 prev[i] = j
                
#     best = max(range(len(a)), key=lambda x: dp[x])
#     res = []
            
#     idx = best
#     while idx > -1:
#         res.append(a[idx])
#         idx = prev[idx]

#     return dp[best], res[::-1]


# def test():
#     # s1 = [1, 2, 3, 4, 5, 6]
#     # s2 = [3, 4, 6, 8, 9]
#     # print(lcs(s1, s2))    
#     print(*lis([1, 4, 3, 8, 5, 9]))


        
# test()


# def search_substring(s, sub):
#     t = sub + '@' + s
#     match = [0] * len(t)
#     res = []

#     for i in range(1, len(t)):
#         p = match[i - 1]

#         while p > 0 and t[i] != t[p]:
#             p = match[p - 1]

#         if t[i] == t[p]:
#             p += 1

#         match[i] = p

#         if p == len(sub):
#             res.append(i - 2 * len(sub)) 
            
#     return res

# l = 'ababa'
# test = search_substring(l, 'aba')
# print(test)

# for i in test:
#     print(l[i])



# lst = [1, 2, 3, 4, 5, 6, 7, 8, 3, 5, 1, 10]


# print(min(lst[5:], key=lambda x: lst[x]))
# print(lst[10])


# class Cat:
#     eyes = 2
#     def __init__(self, name):
#         self.name = name
#         self.hungry = 5
#     def eat(self):
#         self.hungry -= 2

# my_cat = Cat('Pussy')
# print(my_cat.eyes)
# my_cat.eat()
# print(my_cat.hungry)

























































    
    
    
    
    
    
    
