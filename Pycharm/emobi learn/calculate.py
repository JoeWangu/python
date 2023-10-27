def triangle(width, length):
    area = (width * length) / 2
    print(area)


def rectangle(width, length):
    area = width * length
    print(area)


def square(width, length):
    area = width * length
    print(area)


def userinput():
    while True:
        try:
            width: int = int(input("Enter the width: "))
            height: int = int(input("Enter the height: "))
            shape = input("Use T for triangle, R for rectangle and S for square to find area /n" + "Enter the shape: ")
            if shape.lower() == "t":
                return triangle(width=width, length=height)
            elif shape.lower() == "r":
                return rectangle(width=width, length=height)
            elif shape.lower() == "s":
                return square(width=width, length=height)
            else:
                print("Input the correct values")
        except ValueError:
            return print("Please enter an integer value for width and height.")


userinput()
