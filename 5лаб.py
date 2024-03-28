# 1
# import random
# a = []# b = int(input())
# for i in range(10):#     a.append(int(random.random() * 100))
# if b in a:#     print('Поздравляю, Вы угадали число!')
# else:#     print('Нет такого числа!')
# 2
# import random# a = []
# for i in range(10):#     a.append(int(random.random() * 100))
# for i in range(9):#     c = 0
#     for n in range(i + 1):#         if a[i] == a[n]:
#             c += 1#         if c > 1:
#             print(a[i])#             break
# print('***Для проверки:', a)#
# 3
# calendar = tuple(['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su'])# print('сколько выходных на неделе Вы хотите: ', end='')
# a = int(input())# print('Ваши выходные дни: ', end='')
## for i in range(a, 0, -1):
#     print(calendar[len(calendar) - i], ' ', end='')# print('')
# print('Ваши рабочие дни: ', end='')# for i in range(7 - a):
#     print(calendar[i], ' ', end='')
# 4
# import random
# StudentsMD = ['Алексеев', 'Тянутова', 'Керган', 'Головченко', 'Иванов', 'Здобнов', 'Куськова', 'Маценко', 'Уланова', 'Лашкова']
# StudentsDD = ['Аузяк', 'Ахмедов', 'Васильев', 'Жарко', 'Лыткин', 'Рахимов', 'Сидорова', 'Мухин', 'Иванов', 'Обрывалина']
# team = tuple(random.sample(StudentsMD, 10)[:5] + random.sample(StudentsDD, 10)[:5])
# print(StudentsMD)
# print(StudentsDD)
# print(team)
# team = tuple(sorted(list(team)))
# if "Иванов" in team:
#     print (list(team).count("Иванов"))
# else:
#     print("No ")







