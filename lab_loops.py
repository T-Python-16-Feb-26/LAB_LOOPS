
numbers = range(45,210)
for n in numbers:
    if n ==100:
        continue
    elif n ==205:
        break
    print(n)

print('the number is end')

user = "what is the product of 7 * 24 = "
while input(user) !="168":
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")
