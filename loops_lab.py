# =========================
# LAB_LOOPS - Solutions
# =========================

# 1) range from 45 to 210
#    print elements
#    skip 100
#    break at 205

print("Q1) Range 45 to 210 (skip 100, break at 205):")
for num in range(45, 211):  # 211 عشان تشمل 210
    if num == 100:
        continue  # تخطي 100
    if num == 205:
        break     # وقف عند 205 (لا يطبعها)
    print(num)

print("\n" + "="*30 + "\n")

# 2) while loop + input
#    ask: product of 7 * 24
#    if correct -> exit and print success
#    if wrong -> keep asking

correct_answer = 7 * 24

while True:
    user_answer = int(input("Q2) what is the product of 7 * 24 ? "))

    if user_answer == correct_answer:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")

print("\n" + "="*30 + "\n")

# Bonus: Sum of Even Numbers
# Ask user for positive integer n
# Sum even numbers between 1 and n inclusive

n = int(input("Bonus) Enter a positive integer: "))

sum_even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers between 1 and {n} is {sum_even}.")
