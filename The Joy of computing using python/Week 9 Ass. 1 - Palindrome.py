# # The Joy of Computing using Python Week 9 (12/11/2020)

# Given a string, write a program to check if it is palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as string. 
# For example, "NITIN" is a palindrome but "AMIT" is not.

# Input Format:
# The first line of input contains the string (all characters in lower case) which has to be checked.

# Output Format:
# Print 'YES' or 'NO' accordingly.

# Example-1:

# Input:
# amit

# Output:
# NO

# Example-2:

# Input:
# nitin

# Output:
# YES

# Explanation: 
# In the first example, "amit" is not a palindrome as reverse of "amit" is "tima". Whereas in example 2, "nitin" is a palindrome as reverse of "nitin" is "nitin"







def pali(str):
  str1 = str[::-1]
  
  if str1 == str:
    return 'YES'
  else:
    return 'NO'
  
s = input()
print(pali(s), end='')
