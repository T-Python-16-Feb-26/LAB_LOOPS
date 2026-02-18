num= int(input("enter a positive integer:"))
sum_even = 0
for i in range (1,num+1):
      if i % 2 ==0:
         sum_even += i

print(f"the sum of even number between 1 and {num} is {sum_even}")