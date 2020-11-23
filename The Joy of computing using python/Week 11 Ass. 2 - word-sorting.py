# # The Joy of Computing using Python Week 11 (23 Nov 2020)

# Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# Input Format:
# The first line of input contains words separated by the comma.

# Output Format:
# Print the sorted words separated by the comma.

# Example:

# Input:
# without,hello,bag,world

# Output:
# bag,hello,without,world



s = input().split(',')

s.sort()
for i in range(0,  len(s)):

    if i != len(s) - 1:    
        print(s[i], end=',')
    else:
        print(s[i], end='')
