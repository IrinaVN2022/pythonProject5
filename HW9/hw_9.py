# 2.напишіть функцію, яка перевірить, чи дане число є парним чи непарним
# ТА ПОКРИЙТЕ ЇЇ ТЕСТАМИ


def odd_or_even_number(numb):
    """
    Function to check if the given number is odd or even

    Args: any type (int)

    Returns: Even|Odd

    """

    assert isinstance(numb, int), 'argument mast be int'
    return f'{numb} is an Even number' if numb % 2 == 0 else f"{numb} is an Odd number"


if __name__ == '__main__':
    numb = 5
    print(odd_or_even_number(numb))
