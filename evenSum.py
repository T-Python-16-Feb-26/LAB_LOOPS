
n =int( input("please provide a number:"))
sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum += i
        

print(f"sum of all previous even numbers between {1} and {n} is:{sum}")