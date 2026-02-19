

list_of_number = range(45, 210)

for num in list_of_number:
    if num == 100:
        continue

    if num == 205:
        break 
    print(num)


question = "what is the produt of 7*24?"
while int(input(question)) != 168:
    print("Your Answer is wrong try again..")
else: 
    print("your answer is correct")
