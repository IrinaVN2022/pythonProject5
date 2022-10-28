from random import randint
from math import fabs
import time


def generated_number():
    """return: random integer between 1 and 100 """
    AI_result = randint(1, 100)
    return AI_result


def user_number(begin, end):
    """ Function that returns a user guessed number between 1 and 100"""
    while True:
        user_result = input("Please enter your number (1 - 100) : ")
        if user_result.isdigit() and 1 <= int(user_result) <= 100:
            return int(user_result)
            break
        else:
            print("Incorrect number")


def some_msg(AI_num):
    """Function that corresponds to whether the user guessed"""
    while True:
        my_num = user_number(1, 100)
        if AI_num == my_num:
            print('congratulation')
            break
        elif 1 <= fabs(AI_num - my_num) <= 4:
            print('hot')
        elif 5 <= fabs(AI_num - my_num) <= 10:
            print('warm')
        elif fabs(AI_num - my_num) > 10:
            print('cold')


def next_game():
    """ Function that asks to continue the game"""
    while True:
        user_answer = input('play again? (Y/N):  ')
        if user_answer in ['Y', 'N', 'y', 'n']:
            return user_answer
            break


def timeit(func):
    """ decorator that measures and displays the execution time of a function in seconds"""
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


if __name__ == '__main__':
    pass
