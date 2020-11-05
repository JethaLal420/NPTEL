# # The Joy of Computing using Python Week 8 (05/11/2020)

# Write a Python program to add the digits of a positive
#  integer repeatedly until the result has a single digit.

# Input Format:
# The first line of the input contains a number n.

# Output:
# Print the resultant number

# Example:
# Input:
# 48

# Output:
# 3

# Explanation: If you add digits 4 and 8, you will get 12. 
# Again adding 1 and 2 will give 3 which is a single digit and hence the answer.




if __name__ == "__main__":
    n = int(input())
    while(True):
        sum = 0
        while(n > 0):
            tmp = n%10
            sum = sum + tmp
            n = n // 10
        if sum < 10:
            n = sum
            break
        else:
            n = sum
    print(n, end="")