import sys

row, col, B = map(int,sys.stdin.readline().split())
maps = []

for i in range(row):
    maps.append(list(map(int,sys.stdin.readline().split())))

def get_time(maps,B,target):
    bag = B
    time = 0
    tmp_map = map(lambda x:map(lambda y:y-target,x),maps)
    for i in tmp_map:
        for j in i:
            if j<0:
                time-=j
                bag+=j
            elif j>0:
                time+=2*j
                bag+=j
    
    if bag < 0:
        return 9999999999999999999
    else:
        return time

min = 999999999999999999
min_i = 0
list_time = []

for i in range(0,256):
    list_time.append(get_time(maps,B,i))

for i in range(0,len(list_time)):
    if list_time[i]<=min:
        min = list_time[i]
        min_i = i

print(min,min_i)