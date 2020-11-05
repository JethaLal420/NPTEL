# # The Joy of Computing using Python Week 8 (05/11/2020)

# Write a Python program to push all zeros to the end of a given list a. 
# The order of the elements should not change.

# Input Format:
# Elements of the list a with each element separated by a space.

# Output Format:
# Elements of the modified list with each element separated by a space. 
# After the last element, there should not be any space.

# Example:

# Input:
# 0 2 3 4 6 7 10

# Output:
# 2 3 4 6 7 10 0

# Explanation:
# There is one zero in the list. 
# After pushing it at the end the elements of the list becomes 2 3 4 6 7 10 0. 
# The order of other elements remains the same.





n = input().split()

counter = 0

for i in n:
    if i == '0':
        n.remove(i)
        counter += 1
        n.append(i)

for i in range(0, len(n)):
    if i == len(n) - 1:
        print(int(n[i]), end = "")
    else:
        print(int(n[i]), end = " ")