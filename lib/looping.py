#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!")

int_list = [1, 2, 3, 4, 5]
def square_integers(int_list):
    squared_numbers = []
    for num in int_list:
        square_the_numbers = num ** 2
        squared_numbers.append(square_the_numbers)
    return squared_numbers

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)