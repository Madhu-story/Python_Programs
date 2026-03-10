# Getting the largest of 3 numbers from the given list:

numbers = [25, 76, 3, 13, 96, 56, 77, 45, 38, 16, 84, 62, 11, 29]

first = second = third = 0
for num in numbers:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second:
        third = second
        second = num
    elif num > third:
        third = num
print(f"The first greater number is {first}")
print(f"The first greater number is {second}")
print(f"The first greater number is {third}")
