# Check whether the given number is Prime or not:

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is 'NOT A PRIME NUMBER'.")
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
        
    if prime:
        print(f"The given number, {num} is 'PRIME NUMBER'.")
    else:
        print(f"The given number, {num} is 'NOT PRIME NUMBER'.")
        
        
