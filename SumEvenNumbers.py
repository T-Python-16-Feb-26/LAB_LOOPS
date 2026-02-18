num=int(input("Enter a positive integer: "))

total=0
for i in range(0,num+1,2):
    total+=i  
    
        
print(f"The sum of even numbers between 1 and {num} is: {total}")