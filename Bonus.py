n = 0
while n < 1:
    n = int(input("Enter a positive integer: "))

j = 0
for i in range(2,n+1,2):
    j = i+j
    
print(f"The sum of even numbers between 1 and {n} is {j}.")
    