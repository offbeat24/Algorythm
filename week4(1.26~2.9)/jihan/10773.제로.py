n = int(input())
list = []

for i in range(n):
  new = int(input())
  if new == 0:
    del list[len(list)-1]
  else:
    list.append(new)

print(sum(list))