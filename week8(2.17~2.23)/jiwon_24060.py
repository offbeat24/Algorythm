import sys
import math

N,K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
visit = []

def merge(left_arr, right_arr):
  #print("left_arr : ", left_arr)
  #print("right_arr : ", right_arr)
  lIter , rIter = 0, 0
  merged = []

  while lIter < len(left_arr) and rIter < len(right_arr):
    if left_arr[lIter] < right_arr[rIter]:
      visit.append(left_arr[lIter])
      merged.append(left_arr[lIter])
      lIter += 1
    else:
      visit.append(right_arr[rIter])
      merged.append(right_arr[rIter])
      rIter += 1

  if lIter < len(left_arr):
    while lIter < len(left_arr):
      visit.append(left_arr[lIter])
      merged.append(left_arr[lIter])
      lIter += 1

  if rIter < len(right_arr):
    while rIter < len(right_arr):
      visit.append(right_arr[rIter])
      merged.append(right_arr[rIter])
      rIter += 1
  return merged


def mergeSort(arr):
  if len(arr) > 1:
    mid = math.ceil(len(arr) / 2)
    left_arr = mergeSort(arr[0:mid])
    right_arr = mergeSort(arr[mid:len(arr)])

    return merge(left_arr, right_arr)
  return arr


mergeSort(arr)

if K > len(visit):
  print(-1)
else:
  print(visit[K - 1])
