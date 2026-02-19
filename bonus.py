n:int = input("Enter a positive integer: ")
total:int = 0
for num in range(0,int(n)+1,2):
    total += num
print(f"The sum of even numbers between 1 and {n} is: {total}")