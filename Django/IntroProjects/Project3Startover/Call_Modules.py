def import1():
    #import main
    #import main2

    #main.calc102()

    #ANOTHER  way of doing 
    #calling a specific module instead of the whole
    #from main import calc102

    #calc102()
    print()


def import2():
    import numbers
    from utils import find_max

    #numbers = int(input('input numbers ')) not working out
    numbers = [10,3,4,56,7]
    maximum = find_max(numbers)
    print(maximum)


def import3():
    from main2 import randoms
    randoms()
    

import3()