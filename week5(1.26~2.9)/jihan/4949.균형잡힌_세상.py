import sys

def not_isalnum(string):
    if str.isalnum(string) or string == ' ':
        return False
    else:
        return True

while 1:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    
    new_str = ''.join(filter(not_isalnum, string))
    
    stack = []
    for i in new_str:
        if len(stack)==0:
            stack.append(i)
        elif stack[len(stack)-1]=='(' and i == ')':
            del stack[len(stack)-1]
        elif stack[len(stack)-1]=='[' and i == ']':
            del stack[len(stack)-1]
        else:
            stack.append(i)
    
    if stack == ['.']:
        print('yes')
    else:
        print('no')