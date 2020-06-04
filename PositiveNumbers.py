#Taking input from user
list1 = input().split()
num = 0

# using while loop
while (num < len(list1)):

    # checking condition
    if (int(list1[num]) >= 0):
        print(list1[num], end=" ")

    # increment num
    num += 1
