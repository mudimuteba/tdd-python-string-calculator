import re

def add(numbers):
    if numbers == '': return 0

    numbers = map(int, re.findall(r"-?\d+", numbers))
    numbers = filter(lambda x: x < 1000, numbers)
    negative_numbers = filter(lambda x: x < 0, numbers)

    if negative_numbers: raise Exception('negatives not allowed ' + str(negative_numbers))

    return sum(numbers)