# noinspection PyUnusedLocal
import re
def fizz_buzz(number):
    #conver to string to use find
    str_num = str(number)

    #find 3 in string
    three = re.findall('3', str_num)
    #find 5 in string
    five = re.findall('5', str_num)

    if ((number % 3 == 0) and (number % 5 == 0)) or (three and five):
        return "fizz buzz"
    elif (number % 3 == 0) or (three):
        return "fizz"
    elif (number % 5 == 0) or (five):
        return "buzz"
    else:
        return number


print fizz_buzz(546)