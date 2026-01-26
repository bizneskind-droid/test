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


# a, b, c = int(input()), int(input()), int(input())
# up = -b / (2 * a), (4 * a * c - b ** 2) / (4 * a)
# print(up)


# n = int(input())
# b = ()
# for i in range(n):
#     a = input()
#     print(a)
#     if a[-1] > 3:
#         b += (a,)
# print()
# print(b, sep='\n') 


print()




















