#1. Print sum of numbers from 1 to n, where you take n as input from user

number = int(input())

sum = 0
for n in range(number + 1):
    sum += n
print(sum)

# solution without a loop
# number = int(input())
# result = sum([num for num in range(number + 1)])
# print(result)




# 2. Print sum of squares of numbers from 1 to n, where you take n as input from user
# number = int(input())

# sum = 0
# square = 0
# for n in range(number + 1):
#     square = n**2
#     sum += square

# print(sum)

#solution without a loop
# number = int(input())
# result = sum([pow(num,2) for num in range(number + 1)])
# print(result)


# 3. Print result of adding all even numbers and subtracting all odd numbers from 1 to n, where you take n as input from user

# number = int(input())

# result = 0
# for n in range(number + 1):
#     if n % 2 == 0:  # adding all even numbers
#         result += n
#     else:
#         result -= n
# print(result)

#solution without a loop
# number = int(input())
# result = 0
# sum_even_numbers = sum([num for num in range(number +1) if num % 2 == 0])
# sum_odd_numbers = sum([num for num in range(number +1) if num % 2 == 1])
# result = sum_even_numbers - sum_odd_numbers
# print(result)