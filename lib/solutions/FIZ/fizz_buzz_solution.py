# noinspection PyUnusedLocal
def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number



def test(num):
    num2 = str(num)
    if num2.find('3'):
        print 'there is a 3'
    else:
        print 'no'

test(12)