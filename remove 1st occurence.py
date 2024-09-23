#REMOVING THE FIRST OCCURENCE OF AN ELEMENT IN A LIST
l = []
n = int(input("ENTER THE RANGE OF THE LIST :"))
for i in range(n):
  lis = int(input())
  l.append(lis)
r = int(input("ENTER THE ELEMENT YOU WANT TO REMOVE:"))
l.remove(r)
print(l)
