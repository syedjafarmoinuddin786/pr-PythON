#TO FIND THE POSITION OF MIN AND MAX ELE IN LIST
l = []
n = int(input("ENTER THE RANGE OF THE LIST:"))
for i in range(n):
  lis = int(input())
  l.append(lis)
ma = max(l)
mi = min(l)
pos_max = l.index(ma)
pos_min = l.index(mi)
print(pos_max)
print(pos_min)
