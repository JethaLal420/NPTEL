# # The Joy of Computing using Python Week 9 (12/11/2020)

# Given a string S having characters from English alphabets ['a' - 'z'] and '.' as the special character (without quotes). 
# Write a program to construct the lexicographically smallest palindrome by filling each of the faded character ('.') with a lower case alphabet.

# Definition:
# The smallest lexicographical order is an order relation where string s is smaller than t, given the first character of s (s1 ) is smaller than the first character of t (t1 ), or in case they
# are equivalent, the second character, etc.

# For example "aaabbb" is smaller than "aaac" because although the first three characters
# are equal, the fourth character b is smaller than the fourth character c. 

# Input Format: 
# String S

# Output Format: 
# Print lexicographically smallest palindrome after filling each '.' character, if it
# possible to construct one. Print -1 otherwise.

# Example-1

# Input:
# a.ba

# Output:
# abba


# Example-2:

# Input:
# a.b

# Output:
# -1

# Explanation: 
# In example 1, you can create a palindrome by filling the '.' character by 'b'.
# In example 2, it is not possible to make the string s a palindrome.



def small_pal(str):
    revStr = str[::-1]

    while(True):
        pos = str.find('.')
        if pos == -1:
            break
        else:
            if revStr[pos] == '.' and str != revStr and pos == len(str)/2 + 1:
                break
            else:
                if revStr[pos] == '.':
                    str = str.replace('.', 'a', 1 )
                else:
                    str = str.replace('.', revStr[pos], 1)
                

    revStr = str[::-1]
    if str == revStr:
        return str
    else:
        return -1



s = input()

print(small_pal(s), end='')
