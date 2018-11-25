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

    #fizz buzz logic
    if (number % 3 == 0) or (three):
        message = "fizz "
    if (number % 5 == 0) or (five):
        message += "buzz "

    #deluxe logic
    if ((number % 3 == 0) and (three)) or ((number % 5 == 0) and (five)):
        #if even then deluxe else fake deluxe
        if (number % 2 == 0):
            message += "deluxe"
        else:
            message += "fake deluxe"

    #None of the above then is a plain number
    if message == "":
        message = str_num

    return message.strip()