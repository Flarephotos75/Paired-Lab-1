def return_10():
    return 5 + 5

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2 

def length_of_string(string_length):
    return len(string_length)

def join_string(string_1, string2):
    return string_1 + string2

def add_string_as_number(number1, number2):
    converted_number_1 = int(number1)
    converted_number_2 = int(number2)
    return converted_number_1 + converted_number_2

months = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
 }

def number_to_full_month_name(month_number):
    return months[month_number]

# month_number is supplied by the test function and is sent to full_month function which then pulls the correspnding 
# as short month variable, which is then shortened to the first three letters by adding the slice of [0:3] and 3 is always one more than character we want. 

def number_to_short_month_name(month_number):
    short_month = number_to_full_month_name(month_number)
    return short_month[0:3]

def volume_of_cube(length):
    return length * length * length

def reverse_string(string):
    reversed = string[::-1]
    return reversed