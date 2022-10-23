'''1.Є дікт, невідомого наповнення. В дікті присутні ключі, занченням для яких є дікти невідомого наповнення в яких можуть
бути аналогічні вкладені дікти.
Напишіть функцію, яка дістане всі ключі зі значеннями не-діктами з усіх рівнів вкладення,
помістить на один рівень в окремий дікт і поверне цей дікт.
2. Напишіть докстрінг для цієї функці.'''
def choice_not_dict (dictionary):
    """ argument: dictionary
        type argument: dict
        return:a function that will retrieve all keys with non-dict values from all nesting levels,
        will place one level into a separate dict and return that dict"""

    global new_mass
    for elem in dictionary:
        if isinstance(dictionary[elem], dict):
            choice_not_dict(dictionary[elem])
        else:
            new_mass.append(dictionary[elem])
    return new_mass


mass = {'first': {'classic': {'fish': 'buyabes', 'chikken': 'bulion', 'beef': ('lagman', 'bograch')},
                  'vegan': ('mushroom', 'broccoli')}, \
        'main': {'dish': ('steak', 'boiled fish', 'fried fish', 'omelet'),
                 'side dish': {'potato': ('puree', 'free'), 'cereals': ('rice', 'lentils', 'couscous')}}, \
        'drink': ('tea', 'juice', 'coffe')}
new_mass = []
print('choice_new_mass:', choice_not_dict(mass))
