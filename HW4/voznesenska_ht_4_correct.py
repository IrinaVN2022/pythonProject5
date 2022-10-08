# 1.Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран
# кількість слів, які містять дві голосні літери підряд.

raw_string = "Hello my dear friend. oo aio How are you?"
word_counter = 0
cods = [69, 73, 79, 65, 85, 89, 97, 121, 117, 111, 105, 101]
# for i in raw_string.split():
#     flag=False
#     for j in range(len(i)-1):
#         if ord(i[j]) in cods and ord(i[j+1]) in cods:
#             flag=True
#     if flag:
#         print(i)
#         word_counter+=1

letters = 'aeoui'
for word in raw_string.split():
    for idx in range(len(word) - 1):
        if word[idx] in letters and word[idx + 1] in letters:
            print(word)
            word_counter += 1
            break

print('Кількість слів, в яких є дві голосні підряд: ', word_counter)

'''2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245,
 "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
 Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною
 і максимальною ціною. Наприклад:
lower_limit = 35.9
upper_limit = 37.339
> match: "x-store", "main-service"'''

data_dict = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
             "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
dict_range = {k: v for k, v in data_dict.items() if 38 < v < 48}
print('dict_range:', dict_range)
print('shops in the range_38-48:', list(dict_range.keys()))
