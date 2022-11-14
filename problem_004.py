# 1. Take n as input and print the following pattern
# n = 6
# 
# *
# **
# ***
# ****
# *****
# ******

number_of_lines = int(input())
result = '*'
for line in range(number_of_lines + 1):
    result = '*' * line
    print(result)

# 2. Print the following pattern where n is the input.
# n = 6
# 
#      *
#     **
#    ***
#   ****
#  *****
# ******

# number_of_lines = int(input())
# result = '*'
# for line in range(number_of_lines + 1):
#     result = ('*'* line).rjust(number_of_lines + 1)
#     print(result)

# 3. Print the following pattern and where n is the input.
# n = 6
# 
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

# number_of_lines = int(input())
# for line in range(number_of_lines):
#     for spaces in range(number_of_lines - line - 1):
#         print(' ', end='')
#     for stars in range(2 * line + 1):
#         print('*', end='')
#     print()

#4. Print the following pattern where n is the input.
# n = 6
# 
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

# number_of_lines = int(input())
# for line in range(number_of_lines): # the first 6 lines = upper pyramid
#     for spaces in range(number_of_lines - line - 1):
#         print(' ', end='')
#     for stars in range(2 * line + 1):
#         print('*', end='')
#     print()

# for line in range(number_of_lines - 1): # the last 5 lines = downward pyramid
#     for spaces in range(line + 1):
#         print(' ', end='')
#     for stars in range(2 * (number_of_lines - line - 1) - 1):
#         print('*', end='')
#     print()
