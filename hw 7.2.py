def check(func):
    def inside():
        try:
            func()
        except ZeroDivisionError:
            print("Can't divide by zero")
        except ValueError:
            print("Enter a number")
    return inside

@check
def calc():
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))
        num3 = int(input('Enter another number: '))
        operation = input('What are we going to do with these numbers? 1-+, 2 - -, 3-*, 4-/: ')

        if operation == '1':
            print(num1 + num2 + num3)
        elif operation == '2':
            print(num1 - num2 - num3)
        elif operation == '3':
            print(num1 * num2 * num3)
        elif operation == '4':
            if num2 == 0 or num3 == 0:
                raise ZeroDivisionError('Can`t divide by zero')
            print(num1 / num2 / num3)
        else:
            print("Invalid operation")
    except ValueError:
        print("Enter valid numbers")

calc()
