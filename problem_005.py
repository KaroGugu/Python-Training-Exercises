# print the following pattern
# n = 6
# 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

number_of_lines = int(input())
result = 1
for line in range(1, number_of_lines + 1):
    for number in range(1, line + 1):
        print(line, end=' ')
    print()

# print the following pattern
# n = 6
# 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

# number_of_lines = int(input())
# for line in range(number_of_lines + 1):
#     for number in range(1, line + 1):
#         print(number, end=' ')
#     print()

# print the following pattern
# n = 6
# 
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 6 5 4 3 2 1

# number_of_lines = int(input())
# for line in range(number_of_lines):
#     for number in range(line + 1, 0, - 1):
#         print(number, end=' ')
#     print()

# print the following pattern
# n = 6
# 
#           1
#         2 1
#       3 2 1
#     4 3 2 1
#   5 4 3 2 1
# 6 5 4 3 2 1

# number_of_lines = int(input())
# for line in range(number_of_lines):
#     for number in range(number_of_lines - line - 1):
#         print(" ", end=" ")
#     for number in range(line, -1, -1):
#         print(number +1, end=" ")
#     print()

# print the following pattern
# n = 6
# 
#           1
#         2 1 2
#       3 2 1 2 3
#     4 3 2 1 2 3 4
#   5 4 3 2 1 2 3 4 5
# 6 5 4 3 2 1 2 3 4 5 6

# number_of_lines = int(input())

# for line in range(1,number_of_lines + 1):
#     for number in range(1, (number_of_lines - line) + 1):
#         print(end="  ")
#     for number in range(line, 0, -1):
#         print(number,end=' ')
#     for number in range(2, line + 1):
#         print(number,end=' ')
#     print()

# print the following pattern
# n = 6
# 
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14
# 15 16 17 18 19 20

# number_of_lines = int(input())
# start = 1
# for line in range(1, number_of_lines + 1):
#     for number in range(1, line + 1):
#         print(start, end=' ')
#         start += 1
#     print()
