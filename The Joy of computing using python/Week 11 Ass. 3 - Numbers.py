# # The Joy of Computing using Python Week 11 (23 Nov 2020)


Write a program, which will find all such numbers between m and n (both included) such that each digit of the number is an even number.

Input Format:
The first line contains value m and n separated by a comma.

Output Format:
The numbers obtained should be printed in a comma-separated sequence on a single line.

Constraints:
1000<=m<=9000
1000<=n<=9000





def func(d):
    
    while d > 0:
        tmp = d % 10
        d = d // 10
        if tmp % 2 != 0:
            return 0
        
    return 1

    # return 0

    
s = input().split(',')

tmp = int(s[0])
flag = 0

while tmp <= int(s[1]):

    if flag == 0:
        re = func(tmp)
        
        if re:
            print(tmp, end='')
            flag = 1
    else:
        re = func(tmp)
        if re:
            print(','+str(tmp), end='')
    tmp += 2
