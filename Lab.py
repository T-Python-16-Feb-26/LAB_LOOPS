some_number = range(45,211)
for number in some_number:
    if number == 100:
        continue
    if number == 205:
        break
    print(number)

user = "What is the profuct of 7 * 24? "
while input(user) != "168":
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")