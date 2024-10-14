# TO count the no.of vowels present in the string
print("ENTER THE STRING:")
s = input()
for i in s:
  if i == 'a' or i == 'A' or  i == 'e' or i == 'E' or  i == 'i' or i == 'I' or  i == 'o' or i == 'O' or  i == 'u' or i == 'U':
    count = count + 1 
  else:
    print("there are no vowels in this string")
