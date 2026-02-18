number = int(input("Enter a positive number?"))
total = 0 
for num in range (1, number+1):
    if num % 2 == 0:
        total += num

print ("the sum of even number between 1 and", number , "is", total)