#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "admin" and password == "12345":
        message = "Access granted"
    elif username == "ADMIN" and password == "12345":
        message = "Access granted"
    else:
        message = "Access denied"
    return message

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        report = "It's brisk out there!"
    elif temperature >= 40 and temperature < 65:
        report = "It's a little chilly out there!"
    elif temperature > 85:
        report = "It's too dang hot out there!"
    else:
        report = "It's perfect out there!"
    return report

def fizzbuzz(num):
    # your code here
    if num % 15 == 0:
        note = "FizzBuzz"
    elif num % 3 == 0:
        note = "Fizz"
    elif num % 5 == 0:
        note = "Buzz"
    else:
        note = num
    return note
    

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "/":
        answer = num1 /num2
    elif operation == "*":
        answer = num1 * num2
    else:
        print("Invalid operation!")
        answer = None
    return answer
