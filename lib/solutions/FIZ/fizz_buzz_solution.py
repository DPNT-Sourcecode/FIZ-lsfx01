# noinspection PyUnusedLocal
import re
def fizz_buzz(number):
    #conver to string to use find
    str_num = str(number)

    #find 3 in string
    three = re.findall('3', str_num)
    #find 5 in string
    five = re.findall('5', str_num)

    #find 3 or five in number
    if(three == '3' and five == '5'):
        bool_fizz_buzz = 3
    elif (three == '3'):
        bool_fizz_buzz = 1
    elif (five == '5'):
        bool_fizz_buzz = 2
    else:
        bool_fizz_buzz = 0

    if ((number % 3 == 0) and (number % 5 == 0)) or (bool_fizz_buzz == 3):
        return "fizz buzz"
    elif (number % 3 == 0) or (bool_fizz_buzz == 1):
        return "fizz"
    elif (number % 5 == 0) or (bool_fizz_buzz == 2):
        return "buzz"
    else:
        return number



print fizz_buzz(12345)