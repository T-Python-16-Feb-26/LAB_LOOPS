# Part 1 : For loop from 45 to 209, skip 100, break at 205
for num in range(45, 210):
    if num == 100:
        continue  
    print(num)
    if num == 205:
        break     

# Part 2: While loop asking user for 7 * 24
result_prompt = "Enter result of 7 * 24: "

while input(result_prompt) != "168":
    print("Your Answer is wrong try again..")

else:
    print("You answered this Question correctly")
