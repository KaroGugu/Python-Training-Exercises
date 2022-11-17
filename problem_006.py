# Given an integer n, print the following series upto n elements.

# 1. list of first n whole numbers
# loop over all numbers and check if they belong to your series, and stop when you found N

# whole numbers -  numbers without fractions, decimals, and negative numbers. It is a set of only positive numbers, including 0

#solution with for-loop
# numbers = int(input())

# list_whole_numbers = []
# for number in range(numbers):
#     list_whole_numbers.append(number)
# print(list_whole_numbers)


# another solution with while-loop
# numbers = int(input())

# list_whole_numbers = []
# start = 0

# while start < numbers:
#     list_whole_numbers.append(start)
#     start += 1

# print(list_whole_numbers)




# 2. list of first n natural numbers
# Same as above, but figure out the Nth number in the series and loop only till there.

#natural numbers -  whole numbers excluding 0 => without fractions, decimals, and negative numbers

# solution with for-loop

# numbers = int(input())

# list_whole_numbers = []
# for number in range(1, numbers):
#     list_whole_numbers.append(number)
# print(list_whole_numbers)


# solution with while-loop

# list_whole_numbers = []
# start = 1

# while start < numbers:
#     list_whole_numbers.append(start)
#     start += 1

# print(list_whole_numbers)


# 3. list of first n even whole numbers
# See if you can use the range function smartly to only loop over the required numbers.

# numbers = int(input())

# list_whole_numbers = []
# for number in range(0,numbers, 2):
#     list_whole_numbers.append(number)
# print(list_whole_numbers)

# solution with while-loop

# numbers = int(input())
# list_whole_numbers = []
# start = 0

# while start < numbers:
#     if start % 2 == 0:
#         list_whole_numbers.append(start)
#     start += 1

# print(list_whole_numbers)


# 4. list of first n even natural numbers
# Loop i over range(0,N), and try to derive ith element from the value of i
# (looking at how you determined the Nth element in the 2nd attempt might help)
# numbers = int(input())

# list_whole_numbers = []
# for number in range(1, numbers):
#     if number % 2 == 0:
#         list_whole_numbers.append(number)
# print(list_whole_numbers)

# solution with while-loop

# numbers = int(input())
# list_whole_numbers = []
# start = 1

# while start < numbers:
#     if start % 2 == 0:
#         list_whole_numbers.append(start)
#     start += 1

# print(list_whole_numbers)



# 5. list of first n odd whole numbers
# whole - including 0
# numbers = int(input())

# list_whole_numbers = []
# list_whole_numbers.append(0)

# for number in range(numbers):
#     if number % 2 == 1:
#         list_whole_numbers.append(number)
# print(list_whole_numbers)



# 6. list of first n odd natural numbers
# numbers = int(input())

# list_whole_numbers = []
# for number in range(numbers):
#     if number % 2 == 1:
#         list_whole_numbers.append(number)
# print(list_whole_numbers)