# this code work well when one number is missed in a series of numbers .

numbers = [1, 2, 3, 5]
n = len(numbers) + 1
total_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing_number = total_sum - actual_sum
print("Missing Number:", missing_number)

## OUT PUT:- Missing Number: 4

# ALTERNATIVE SOLUTION ***"This code works well even if some numbers are missing from the sequence."***

numbers = [1, 2, 3, 5]

for i in range(1, max(numbers)+1):
    if i not in numbers:
        print(i)
      
#OUT PUT: 4
