n = int(input("Enter a positive integer: "))
total = 0

for num in range(1, n + 1):
    if num % 2 == 0:
        total += num

print(f"The sum of even numbers between 1 and {n} is {total}.")