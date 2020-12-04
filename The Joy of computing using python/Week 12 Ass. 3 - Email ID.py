# # The Joy of Computing using Python Week 12 (04 Dec 2020)

# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Input Format:
# The first line of the input contains an email address.

# Output Format:
# Print the company name in single line.

# Example:

# Input:
# john@google.com

# Output:
# google



n = input()
l = []
flg = 0
s = ''
for i in n:
    if i == '@':
        flg = 1
        continue
    if i == '.':
        flg = 0
    if flg == 1:
        l.append(i)

print(s.join(l), end='')
