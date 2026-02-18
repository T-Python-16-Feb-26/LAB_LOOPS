user_input=int(input("Enter a positive integer: "))


sum_number= 0
for number in range(1,user_input+1):
    if number %2==0:
       sum_number+=number

print(f"The sum of even numbers between 1 and {user_input} is {sum_number}.")

