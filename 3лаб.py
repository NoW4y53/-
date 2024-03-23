# ЛАБОРАТОРНАЯ 3
# ЗАДАНИЕ 1

# print('введите кол-во слов:')
# n = int(input())
# s = ''
# print('начните вводить слова:')
# for i in range(n):
#     s += str(input())
# print(s)


# 2
# print('начните вводить слова:')
# a = str(input())
# s = ''
# while a != 'stop':
#     s += a
#     a = str(input())
# print(s)

# 3

# print('начните вводить слова:')
# a = str(input())
# if 'ф' in a:
#     print('Ого! Это редкое слово!')
# else:
#     print('Эх, это не очень редкое слово...')

# 4
import random
i, a, b, c, f = 0,0, 0, 0, 0

while i < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(a, '+', b, '=', end=' ')
    c = int(input())
    if (a + b) == c:
        print('Правильно')
        f += 1
    else:
        print('Ответ неверный')
        i += 1
print('Игра окончена. Правильных ответов: ', f)




