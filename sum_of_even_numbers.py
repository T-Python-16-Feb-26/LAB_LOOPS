number=int(input("insert a number: "))

total=0

for i in range(1,number+1):
    if i%2==0:
        total=total+i
        print(total)
print(f"The sum between 1 and {number} is {total}")
