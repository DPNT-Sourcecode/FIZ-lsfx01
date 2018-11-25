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


    #Check if greater than 10 to be deluxe
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

        #If all digits are the same then deluxe
        if same == True:
            message += " deluxe"

    if message == "":
        message = str_num

    return message.strip()

num = 5
print fizz_buzz(num)
print len(fizz_buzz(num))