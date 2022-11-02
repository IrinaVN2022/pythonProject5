# 2.напишіть функцію, яка перевірить, чи дане число є парним чи непарним
# ТА ПОКРИЙТЕ ЇЇ ТЕСТАМИ


def odd_or_even_number(number):
    """
    Function to check if the given number is odd or even

    Args: any type (int)

    Returns: Even|Odd

    """

    assert isinstance(number, int), 'argument mast be int'
    return f'{number} is an Even number' if number % 2 == 0 else f"{number} is an Odd number"


print(odd_or_even_number(89))

assert odd_or_even_number(14) == '14 is an Even number'
assert odd_or_even_number(7) == '7 is an Odd number'
