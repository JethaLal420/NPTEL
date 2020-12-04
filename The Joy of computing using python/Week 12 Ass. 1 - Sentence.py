# # The Joy of Computing using Python Week 12 (04 Dec 2020)


# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalised.

# Input Format:
# The first line of the input contains a number n which represents the number of line.
# From second line there are statements which has to be converted. Each statement comes in a new line.

# Output Format:
# Print statements with each word in capital letters.

# Example:

# Input:
# 2
# Hello world
# Practice makes perfect

# Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT



n = int(input())

l = []

for i in range(0, n):
    j = input()
    l.append(j)

for i in range(0, n):
    if i != n-1:
        print(l[i].upper())
    else:
        print(l[i].upper(), end = '')
