# Write a program to find the factorial of the given number using recursion.

num = int(input("Enter a number: "))

def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)

result = factorial(num)
print(result)