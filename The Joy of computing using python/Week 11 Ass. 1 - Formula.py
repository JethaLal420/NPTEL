# # The Joy of Computing using Python Week 11 (23 Nov 2020)


Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Input Format:
A sequence of values for D with each value separated by a comma.

Output Format:
Print the sequence of Q values with each value separated by a comma.

Example:

Input:
100,150,180

Output:
18,22,24


import math

def func(d):
    c, h = 50, 30
    return math.sqrt((2*c*d)/h)


    # return 0

    
s = input().split(',')

for i in range(0,  len(s)):
    re = func(int(s[i]))

    if i != len(s) - 1:    
        print(round(re), end=',')
    else:
        print(round(re), end='')
