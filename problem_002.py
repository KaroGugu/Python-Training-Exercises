#Given an integer n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird


number = int(input())

if number % 2 == 1:
    print("Weird")
else:
    if number >= 2 and number <= 5:
        print("Not weird")
    elif number <= 20:
        print("Weird")
    else:
        print("Not Weird")

# Another solution:

# if (number % 2 == 1) or (number >= 6 and number <= 20):
#     print("Weird")
# else:
#     print("Not Weird")
