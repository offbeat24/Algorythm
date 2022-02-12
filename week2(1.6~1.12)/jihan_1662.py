import sys
from collections import Counter

string = list(sys.stdin.readline().rstrip())

#print(string)
pointer = 0
cnt = Counter(string)

def confirm(array):
    for i in array:
        if i[0]=='F':
            return True
    return False

while cnt['(']!=0:
    if string[pointer] == ')':
        tmp_ptr = pointer
        while string[tmp_ptr] != '(':
            tmp_ptr-=1
        tmp_len = 0
        for i in string[tmp_ptr:pointer+1]:
            if i[0]=='F':
                tmp_len+=int(''.join(i[1:len(i)]))
            elif not(i=='(' or i==')'):
                tmp_len+=1
        tmp_len = tmp_len*int(string[tmp_ptr-1])
        del string[tmp_ptr-1:pointer+1]
        string.insert(tmp_ptr-1,'F'+str(tmp_len))
        pointer = tmp_ptr-1
    pointer+=1
    cnt = Counter(string)

length = 0
for i in string:
    if i[0]=='F':
        length+=int(''.join(i[1:len(i)]))
    else:
        length+=1
        
print(length)