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

