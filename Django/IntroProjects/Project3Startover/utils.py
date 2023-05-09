#UTILITY functions modules
def find_max(numbers):
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum