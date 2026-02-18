for i in range(45,210):
    if i ==100:
        continue
    if i == 205:
        break
    print(i)


while True:
    user_input = int(input(" what is the product of 7 *24?"))
    if user_input == 168:
        print ("your answered this question correctly")
        break
    else:
        print("your answer is wrong ,try again")
