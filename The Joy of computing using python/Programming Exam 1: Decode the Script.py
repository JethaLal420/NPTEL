## December 13 Programming test - Session 1 (10AM to 11AM) (2020)


# Nandini has a complex matrix script. The matrix script is a N X M grid of strings. It consists of alphanumeric characters and symbols (!,@,#,$,%,&). To decode the script, Nandini needs to read each column and select only the alphanumeric characters and connect them. She reads the column from top to bottom and starts reading from the leftmost column. If there are symbols in the decoded script, then Nandini removes them for better readability. Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

# Input Format

# The first line contains space-separated integers N (rows) and M (columns) respectively. 
# The next N lines contain the row elements of the matrix script separated by space.

# Output Format

# Print the decoded matrix script.

# Sample Input:
# 7 3
# T s i
# h % x
# i  # $
# s M #
# $ a  &
# # t %
# i r !

# Output:
# ThisisMatrix



rc = input().split()

row = int(rc[0])
column = int(rc[1])

arr = []

sy = ['!', '@', '#', '$', '%', '&']

for i in range(0, row):
    j = input().split()
    arr.append(j)

# print(arr)

for i in range(0, column):
    for j in range(0, row):
        tmp = arr[j][i]
        if tmp not in sy:
            print(tmp, end = '')

# print('END')
