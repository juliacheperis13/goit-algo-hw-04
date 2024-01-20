import random


def get_random_numbers(limit, number):
    return [random.randint(0, limit) for _ in range(number)]
