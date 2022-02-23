num = list(input())

arr = []
answer = 1000000
visited = [False] * (len(num))
def num_maker() :
  global answer
  if len(arr) == len(num) :
    if int(('').join(num)) < int(('').join(arr)) :
      answer = min(answer, int(('').join(arr)))
    return
  else :
    for i in range(0, len(num)):
      if visited[i] == False :
        visited[i] = True
        arr.append(num[i])
        num_maker()
        visited[i] = False
        arr.pop()

num_maker()
if answer != 1000000 :
    print(answer)
else :
    print(0)
  