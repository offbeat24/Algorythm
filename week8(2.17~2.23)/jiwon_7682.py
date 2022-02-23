import sys

arr = []
lastTurn = ''

while True:
  input = sys.stdin.readline().rstrip()
  if input == "end":
    break

  arr.append(input)

def checkTurn(s):
  global lastTurn
  Xs, Os = 0,0
  for i in range(len(s)):
    if s[i] == 'X':
      Xs += 1
    if s[i] == 'O':
      Os += 1

  if Xs == Os + 1:
    lastTurn = 'X'
    return True

  if Xs == Os:
    lastTurn = 'O'
    return True

  return False

def checkWin(s):
  global lastTurn
  cases = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  cnt = []

  for case in cases:
    if s[case[0]] == '.':
      continue

    if s[case[0]] == s[case[1]] and s[case[0]] == s[case[2]]:
      if lastTurn == s[case[0]]:
        cnt.append(case)
      else:
        return False

  if len(cnt) == 1:
    return True

  if len(cnt) == 0:
    for i in range(9):
      if s[i] == '.':
        return False
    return True

  if len(cnt) == 2:
    temp = cnt[0] + cnt[1]
    temp = set(temp)
    #print(temp)
    if len(temp) == 5:
      return True
    else:
      return False

  return False

for i in range(len(arr)):
  #print(checkTurn(arr[i]), checkWin(arr[i]))
  if checkTurn(arr[i]) and checkWin(arr[i]):
    print('valid')
  else:
    print('invalid')
