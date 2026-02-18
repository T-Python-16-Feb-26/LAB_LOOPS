# for loop

number_range = (45, 210)

for num in range(45, 210):

    if num == 100:
       continue
      
    elif num == 205:
         break
        
    else:
      print(num)

print()

# while loop

question = "What is the product of 7 * 24 ? "

while input(question) != "168":
    print("Your answer is wrong, try again.")

print("You answered this Question correctly.")