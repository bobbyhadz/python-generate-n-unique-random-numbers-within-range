# Generate N unique random numbers within a range in Python

import random


def gen_random_numbers_in_range(low, high, n):
    return random.sample(range(low, high), n)


# 👇️ [6, 9, 4, 8, 1]
print(gen_random_numbers_in_range(1, 10, 5))

# 👇️ [8, 4, 1, 3, 5]
print(gen_random_numbers_in_range(1, 10, 5))