n= int(input("Enter a positive integer: "))
sum = 0

for x in range(1, n + 1):
    if x % 2 == 0:  
        sum += x 

print(f"The sum of even numbers between 1 and {n} is {sum}.")