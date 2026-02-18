#lab loops

for numbers in range(45,210):
    if numbers == 100:
        continue
    print(numbers)
    if numbers == 205:
        break
print("Done\n\n")

counters = 0
while counters < 10:
    counters += 1
    question = input("what is the product of 7 * 24 ? ")
    if question == "168":
        print("you answered correctly")
        break
    else:
        print("you answered incorrectly")

