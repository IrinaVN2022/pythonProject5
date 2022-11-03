# 2.напишіть функцію, яка перевірить, чи дане число є парним чи непарним
# ТА ПОКРИЙТЕ ЇЇ ТЕСТАМИ

def is_odd(number):
    """
        check if the given number is odd

        Args: integer, float

        Returns: True|False

        """
    if number % 2 != 0:
        return True
    else:
        return False

is_odd(22228880)

assert type(is_odd(56)) == bool
assert type(is_odd(8.8)) == bool
assert is_odd(222) is False
assert is_odd(99) is True