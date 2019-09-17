import re

def add(numbers):
    if numbers == '': return 0

    numbers = re.findall(r"-\d+|\d+", numbers)
    numbers = list(map(int, numbers))
    negative_numbers = filter(lambda x: x < 0, numbers)

    if negative_numbers: raise Exception('negatives not allowed ' + str(negative_numbers))

    numbers = filter(lambda x: x >= 0 and x < 1000, numbers)

    return sum(numbers)