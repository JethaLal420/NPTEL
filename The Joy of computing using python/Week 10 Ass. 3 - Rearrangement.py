# # The Joy of Computing using Python Week 10 (16 Nov 2020)

# Given a list A of elements of length N, ranging from 1 to N. All elements may not be present in the array. If the element is not present then 
#     there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present display -1 at that place.

# Input Format:
# The first line contains n numbers with each number separated by a space.

# Output Format:
# Print the elements of the list after the modification.

# Example:

# Input:
# -1 -1 6 1 9 3 2 -1 4 -1

# Output:
# -1 1 2 3 4 -1 6 -1 -1 9

# Explanation:
# The modified list contains elements such that A[i] = i.



def func(n):
    n.sort()
    
    for i in range(0, int(n[-1]) + 1):
        if n.count(str(i)) == 0:
            print('-1', end = ' ')
        elif i != int(n[-1]):
            print(i, end = ' ')
        else:
            print(i, end = '')

            
            
n = input().split()
re = func(n)

# print(re, end = '' )

