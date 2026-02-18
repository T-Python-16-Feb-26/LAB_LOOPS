
n = int(input("Enter positive number :"))
total = 0
for i in range (1 , n+1):
    if i%2==0:
        total=total+i
        print(total)
print(f'the sum between 1 and {n}is {total}')

