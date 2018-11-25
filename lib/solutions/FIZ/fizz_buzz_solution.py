# noinspection PyUnusedLocal
import re
def fizz_buzz(number):
    #conver to string to use find
    str_num = str(number)

    #find 3 in string
    three = re.findall('3', str_num)
    #find 5 in string
    five = re.findall('5', str_num)

    if (three):
        return "fizz"
    elif (five):
        return "buzz"
    else:
        return number



print fizz_buzz('12')