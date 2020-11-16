# # The Joy of Computing using Python Week 10 (05 Nov 2020)



Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates. 

Input Format:
The first line contains n-1 numbers with each number separated by a space.

Output Format:
Print the missing number

Example:

Input:
1 2 4 6 3 7 8

Output:
5

Explanation:
In the above list of numbers 5 is missing and hence 5 is the input



def func(n):
    n.sort()
    sum2 = 0
    sum1 = ( int(n[-1] ) * ( int(n[-1]) + 1 )) //2
    for i in range(0, len(n)):
        sum2 = sum2 + int(n[i])

    if sum1 == sum2:
        return int(n[-1]) + 1
    
    return sum1 - sum2
    
    
n = input().split()
re = func(n)

print(re, end = '' )
