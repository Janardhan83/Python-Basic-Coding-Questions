# What is an Armstrong Number?
# An Armstrong number is a number where:
# Sum of each digit raised to the power of total digits equals the original number.
# Example:
# 153=1 3 +5 3 +3 3
# Calculation:
# 1 3 +5 3 +3 3 =1+125+27=153What is an Armstrong Number?
# An Armstrong number is a number where:
# Sum of each digit raised to the power of total digits equals the original number.
# Example:
# 153=1 3 +5 3 +3 3
# Calculation:
# 1 3 +5 3 +3 3 =1+125+27=153
num = int(input("Enter a number: "))

temp = num
power = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
  """OUT PUT :-
  Enter a number: 1532
Not Armstrong Number """
