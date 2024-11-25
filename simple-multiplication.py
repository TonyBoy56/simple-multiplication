# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

my_number = 7

def simple_multiplication(number):
    if number % 2 != 0:
        print(number * 8)
    else: 
        print(number * 9)
    
simple_multiplication(my_number)