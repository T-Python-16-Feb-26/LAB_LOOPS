number_user = int(input("Enter a positive integer: "))
total_number = 0

for even in range(1,number_user+1):
    if even %2==0:
        total_number += even

print(f"The sum of even numbers between 1 and {number_user} is : {total_number}")