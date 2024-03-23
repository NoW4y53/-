# Лабораторная работа 4
#
# ЗАДАНИЕ 1
# def d(a):
#     if (a % 3) == 0 and a != 0:
#         return ('делится')
#     else:
#         return ('не делится')
#
# print(d(int(input())))

# 2
# def d(a):
#     if a != 0:
#         return a / 100
#     else:
#         return 'Ошибка'
#
# a = input()
# if a.isdigit():
#     print(d(int(a)))
# else:
#     print('Ошибка')

# 3
# def d(a):
#     if (int(a[0]) * int(a[1])) == (int(a[2][-2:])):
#         return True
#     return False
#
# a = ((input()).split('.'))
# print(d(a))

# 4
# def d(n):
#     fsum, ssum = 0, 0
#     l = len(n) // 2
#     for i in range(l):
#         fsum += int(n[i])
#     for i in range(l, len(n)):
#         ssum += int(n[i])
#     if fsum == ssum:
#         return 'Ваш билет - счастливый'
#     return 'Ваш билет - несчастливый'
# n = str(input())
# print(d(n))

