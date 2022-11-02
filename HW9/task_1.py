# 1. дописати (в тому числі докстрінги) - очікування - прохід тестів

def is_string_capitalized(string):
    """
    Function check if the given string is already capitalised
    Args:
        string: any type (str)

    Returns: True|False


    """
    if string == string.capitalize():
        return True
    else:
        return False