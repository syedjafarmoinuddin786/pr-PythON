# CHECK WHETHER THE STRING IS PALINDROME OR NOT
print('ENTER THE STRING:')
s = input()
r = s[::-1]
if s == r:
  print("IT IS A PALINDROME")
else:
  print("IT IS NOT A PLAINDROME")
