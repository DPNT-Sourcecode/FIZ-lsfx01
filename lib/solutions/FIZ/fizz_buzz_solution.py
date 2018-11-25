# noinspection PyUnusedLocal
import re
def fizz_buzz(number):
    #conver to string to use find
    str_num = str(number)

    #find 3 in string
    three = re.findall('3', str_num)
    #find 5 in string
    five = re.findall('5', str_num)

    message = ""

    if (number % 3 == 0) or (three):
        message = "fizz "
    if (number % 5 == 0) or (five):
        message += "buzz "
    if message == "":
        message = number

    #Check if greater than 10
    if number > 10:
        #Initialize variables
        same = False
        prev = str_num[0]

        #check every char against previous
        for n in str_num:
            if n == prev:
                same = True
            else:
                same = False
                break

        if same == True and message != number:
            message += "deluxe"

    return message

print fizz_buzz(33)

