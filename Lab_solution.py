#loop lab

#for loop
the_numbers= range(45,210)

for number in the_numbers:
    if number==100:
        continue
    if number==205:
        break
    print(number)

print("-"*15)

#while loop

question="what is the product of 7 * 24 ?"
while int(input(question)) != 168:
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")