"""
Write a Python program that prompts the user for a positive integer `n`, 
and then calculates the sum of all even numbers between 1 and `n`, inclusive.

Your program should use a loop (either a `for` loop or a `while` loop) to iterate 
over the numbers between 1 and `n`, and only add the even numbers to the sum.
"""

n = int(input("Enter a positive integer: "))
while n <= 0:
    n = int(input("Please enter a positive integer: "))

sum_even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even = sum_even + i

print("The sum of even numbers between 1 and {} is: {}".format(n, sum_even))