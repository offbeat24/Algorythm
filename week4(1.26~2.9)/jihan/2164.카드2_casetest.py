def card(num):
    print('case: ',num)
    list = [i for i in range(1,num+1)]
    flag = 1

    while(len(list)>1):
        if flag == 1:
            list.pop(0)
            flag = 0
        else:
            list.append(list.pop(0))
            flag = 1
        print(list)

    print(list[0])


for i in range(1,20):
    card(i)