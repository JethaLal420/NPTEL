








def pali(str):
  str1 = str[::-1]
  
  if str1 == str:
    return 'YES'
  else:
    return 'NO'
  
s = input()
print(pali(s), end='')
