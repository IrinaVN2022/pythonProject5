#1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент,
#перетворений на float.
#Якщо перетворити не вдається функція має повернути 0.

def get_float(arg1, arg2=0):

    while True:
        try:
            argum = float(input(arg1))
        except:
            return arg2
            continue
        else:
            break
    return argum
result =  get_float ('Enter your argument:')
print('float_result:', result)
#2. Напишіть функцію, що приймає два аргументи. Функція повинна
#якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
#якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
#у будь-якому іншому випадку повернути кортеж з цих аргументів
def proces (arg1, arg2):
    if (type(arg1) == int or type(arg1) == float) and (type(arg2) == int or type(arg2) == float):
        return arg1*arg2
    elif (type(arg1) == str and type(arg2) == str):
        return arg1+arg2
    else:
        return (arg1, arg2)
print('result of multiplication:', proces(5,6))
print('result of multiplication:', proces(3.2, 50))
print('result of multiplication:', proces(356, 5.0))
print('result of concatenation:', proces('ast','vv'))
print('cortege:', proces(3.2, 'cc'))
'''3.Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
Попросіть користувача ввести свсвій вік.
- якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
- якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
- якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
- якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. 
Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача 
(1 - рік, 22 - роки, 35 - років і тд...). Наприклад :
"Тобі ж 5 років! Де твої батьки?"
"Вам 81 рік? Покажіть пенсійне посвідчення!"
"Незважаючи на те, що вам 42 роки, білетів все одно нема!"
'''


def year(x):
    if 10 <= int(x[len(x) - 2:len(x)]) <= 20:
        return 'років'
    elif 5 <= int(x[-1]) <= 9 or int(x[-1]) == 0:
        return 'років'
    elif 2 <= int(x[-1]) <= 4:
        return 'роки'
    elif int(x[-1]) == 1:
        return 'рік'
def request():
    while True:
        result = input('Введіть свій вік: ')
        if result.isdigit() == False:
            print("Відповідь не правильна! Будь ласка, введіть ціле число!")

        else:
            return result
            break

def kasir():
    age = request()
    if int(age) > 120:
        print("Дані не є вірні! Вкажіть ,будь ласка, Ваш справжній вік!")
    elif int(age) < 7:
        print(f'Тобі ж {age} {year(age)}! Де твої батьки?')
    elif 7 < int(age) < 16:
        print(f'Тобі лише {age} {year(age)},а це е фільм для дорослих!')
    elif int(age) > 65:
        print(f'Вам {age} {year(age)}? Покажіть пенсійне посвідчення!')
    elif '7' in age:
        print(f'Вам {age} {year(age)}, вам пощастить')
    else:
        print(f'Незважаючи на те, що вам {age} {year(age)},білетів всеодно нема!')

kasir()