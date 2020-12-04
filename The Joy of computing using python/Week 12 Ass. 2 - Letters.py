# # The Joy of Computing using Python Week 12 (04 Dec 2020)


Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Input Format:
The first line of the input contains a statement.

Output Format:
Print the number of upper case and lower case respectively separated by a space.

Example:

Input:
Hello world!

Output:
1 9


n = input()
u = 0
l = 0
for i in n:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
print(u, l, end = '')
