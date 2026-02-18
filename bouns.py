print()
num = int(input("Enter Positive Integer:") )
Total= 0
for i in range(1, num + 1 ):
    if i % 2 == 0:
        Total += i
    
print("The sum of even numbers between 1 and", num, "is",Total)