#INTRODUCTORY MODULE
# ctrl + / to comment
import math
#def - define

def input101():
    name = input('enter name ')
    color = input('enter color ')
    print(name + ' likes ' + color)


def calc101():
    weight_lbs = input('enter weight in pounds = ')
    weight_kgs = int(weight_lbs) * 0.45
    print(weight_kgs)


def calc102():
    weight = int(input('enter weight = '))
    unit = input('(L)bs or (K)g: ')
    if unit.upper() == 'L':
        converted_weight = weight * 0.45
        print(f'You are {converted_weight} kilograms')
    elif unit.upper() == 'K':
        converted_weight = weight // 0.45
        print(f'You are {converted_weight} pounds')
    else:
        print('input correct values')


def letters101():
    #course = '''
    #hi john
    #here is our fisrt email to you
    #love lon
    #'''
    #print(course)
    #course2 = 'welcome to python'
    #print(course2[-1])
    #print(course2[0:3]) #same as print(course2[:3])
    #print(course2[:])
    name = 'jennifer'
    print(name[1:-1])


def letters102():
    f_name = 'John'
    l_name = 'Smith'
    #message = f_name + '[' + l_name + ']' + ' is a coder '
    #print(message)
    #same as
    msg = f'{f_name} [{l_name}] is a coder'
    print(msg)


def string101():
    course = 'welcome to python'
    print(len(course)) #count no in string
    print(course.upper()) #convert to uppercase
    print(course.find('o')) #return index of char
    print(course.replace('python' , 'begginers python'))
    print(course.replace('o' , 'i'))
    print('python' in course)


def arithmetics101():
    print(10 % 3) #modulus - returns rem of division
    print(10 // 3) #get interger instead of float after calculation
    print(10 ** 3) #exponent/power(10 to power of 3)
    x = 10
    x += 3 #same as x = x + 3
    print(x)
    #BODMAS bracket exponentiation division multiplication addition subtraction


def math101():
    x = -2.9
    print(round(x)) #round off
    print(abs(x)) #always return no as positive
    print(math.floor(2.9))


def if101():
    is_hot = False
    is_cold = False

    if is_hot:
        print('too hot')
        print('drink more water')
    elif is_cold:
        print('too cold')
        print('wear warm')
    else:
        print('lovely day')
    print('enjoy your day')


def if102():
    price = 1000000
    good_credit = False
    
    if good_credit:
        down_payment = 0.1 * price
        print(f'down payment is ${down_payment}')
    else:
        down_payment = 0.2 * price
        print(f'down payment is ${down_payment}')


def logicoperators101():
    high_income = False
    good_credit = True
    criminal_record = True

    if high_income and good_credit:#and,or
        print('eligible for loan')
    else:
        print('not eligible for loan')
    
    if high_income and not criminal_record:
        print('eligible for loan')


def comparisonoperators101():
    temp = int(input('input temp '))
    if temp >= 30:
        print('hot day')
    elif temp <= 10:
        print('cold day')
    else:
        print('not hot not cold')


def comparisonoperators102():
    name = input('input name ')
    if len(name) < 3:
        print('too short')
    elif len(name) > 20:
        print('too long')
    else:
        print('looks good')


def while101():
    i = 1
    while i <= 5:
        print("#" * i)
        i += 1
    print('done')


def guessing_game101():
    guess_no = 5
    guess_count = 0
    guess_limit = 3
    print('game: guess a number(limit is 3 times)')
    while guess_count < guess_limit:
        guess = int(input('guess: '))
        guess_count += 1
        if guess == guess_no:
            print('correct guess')
            break
    else:
        print('sorry you failed')


def help_prompt101():
    command = ''
    while command != 'quit': #or while true:
        command = input('>').lower()
        if command == 'start':
            print('car started...ready to go!')
        elif command == 'stop':
            print('car stopped.')
        elif command == 'quit':
            quit #or break
        elif command == 'help':
            print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
        else:
            print("i don't understand that!!!")


def help_prompt102():
    command = ''
    started = False
    while command != 'quit': #or while true:
        command = input('>').lower()
        if command == 'start':
            if started:
                print('car already started')
            else:
                started = True
                print('car started...ready to go!')
        elif command == 'stop':
            if not started:
                print('car already stopped!')
            else:
                started = False
                print('car stopped.')
        elif command == 'quit':
            quit #or break
        elif command == 'help':
            print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
        else:
            print("i don't understand that!!!")


def for_loops101():
    #for item in range(5,10,2): #go 2 steps forward
        #print(item)
    prices = [10,20,30]
    total = 0
    for price in prices:
        total += price
    print(f'Total is: {total}')


def nested_loops101():
    for x in range(4):
        for y in range(4):
            print(f'({x},{y})')


def nested_loops102():
    numbers = [5,2,5,2,2]
    for x in numbers:
        output = ''
        for y in range(x):
            output += 'x'
        print(output)


def lists101():
    nos = [10,34,556,88,56,42]
    max = nos[0] #or max = 0
    for no in nos:
        if no > max:
            max = no
    print(max)


def lists_2d101():
    matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    print(matrix[0])
    print(matrix[0][1])
    for row in matrix:
        for item in row:
            print(item)


def lists102():
    numbers = [1,2,3,4,5,2,8]
    numbers2 = numbers.copy()
    print(numbers.index(3))
    print(50 in numbers)
    numbers.insert(0,2)
    numbers.remove(3)
    numbers.pop()
    numbers.sort()
    print(numbers)
    print(numbers.count(2))
    
    uniques = []
    for nums in numbers2:
        if nums not in uniques:
            uniques.append(nums)
    print(uniques)


def tuples101(): #cannot edit(ie. be modified) tuples like in lists/arrays
    numbers = (1,2,3)
    x,y,z = numbers
    print(x + y * z)


def dictionaries101():
    pad = {
'make' : 'xbox',
'age' : 2,
'light' : 'green',
'color' : 'black',
'is_working' : True
    }
    print(pad['color'])
    pad['is_ok'] = 'yes' #add to dictionary
    print(pad['is_ok'])


def dictionaries102():
    phone_number = input('Enter phone number ')
    numbers = {
 '1' : 'one',
 '2' : 'two',
 '3' : 'three',
 '4' : 'four',
 '5' : 'five',
 '6' : 'six',
 '7' : 'seven',
 '8' : 'eight',
 '9' : 'nine',
 '0': 'ten'
    }
    output = ''
    for nums in phone_number:
        output += numbers.get(nums ,'!') + ' '
    print(output)


def emojis101():
    message = input('sentence > ')
    words = message.split(' ')
    emojis = {
        ':)' : '😀',
        ':(' : '😔',
        '(:o' : '😯'
    }
    output = ''
    for word in words:
        output += emojis.get(word , word) + ' '
    print(output)


def parameters101(name): #name is parameter ie. placeholder for functions for receiving informatiom
    print(f'hi {name}')
    print('welcome here')
    #parameters101('John') john and mary are arguments
    #parameters101('Mary')
    #positional arguments vs keyword arguments
    #eg. par('John', 'Mkubwa') - positional
    #par(last_name = 'Mkubwa, first_name = 'John) - keyword(explain what arguments are input)


def retun101(number):
    return number * number
#print(retun101(3)) - done outside code


def reuse_fuction101(message): #from emojis101()
    words = message.split(' ')
    emojis = {
        ":)":"😁",
        ":(":"😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


#message = input('>')
#print(reuse_fuction101(message))


def exceptions101():
    try:
        age = int(input('age: '))
        print(age)
    except ValueError:
        print('invalid value')


nested_loops101()