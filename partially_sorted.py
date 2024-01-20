import random


def get_partially_sorted_numbers(limit, precision):
    original_list = list(range(limit))

    preserve_size = int(precision * len(original_list))

    random.shuffle(original_list)

    start_index = random.randint(0, len(original_list) - preserve_size)
    preserved_subset = sorted(
        original_list[start_index:start_index + preserve_size])

    final_list = original_list[:start_index] + preserved_subset + \
        original_list[start_index + preserve_size:]

    return final_list
