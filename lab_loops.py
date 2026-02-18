# 1) Using range(),  make a range from 45 to 210, 
# using a for loop iterate over the sequence 
# and print the elements. Skip the number 100 and break the loop at 205

for i in range(45, 210):
    if i == 100:
        continue
    elif i == 205:
        break
    else:
        print(i)

# 2) Using a while loop and input
while input("what is the product of 7 * 24 ? ") != "168":
    print("Your Answer is wrong try again..")

else:
    print("You answered this Question correctly")

