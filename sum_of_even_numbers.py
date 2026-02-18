number = int(input("Enter a positive integer: "))
total = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        total += i

print(f"The sum of even numbers between 1 and {number} is {total}.")
