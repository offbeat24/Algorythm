n = int(input())

paper = list()
answer = list(0 for _ in range(3))
for _ in range(n):
    paper.append(list(map(int, input().split())))


def paper_test(x, y, size):
    tmp = paper[x][y]
    for i in range(x+1, x+size):
        for j in range(y+1, y+size):
            if paper[i][j] != tmp:
                return False
    return True


def paper_slicing(x, y, size):

    if paper_test(x, y, size):
        answer[paper[x][y]+1] += 1
    else:
        size //= 3
        paper_slicing(x, y, size)
        paper_slicing(x, y+size, size)
        paper_slicing(x, y+size+size, size)

        paper_slicing(x+size, y, size)
        paper_slicing(x+size, y+size, size)
        paper_slicing(x+size, y+size+size, size)

        paper_slicing(x+size+size, y, size)
        paper_slicing(x+size+size, y+size, size)
        paper_slicing(x+size+size, y+size+size, size)


paper_slicing(0, 0, n)

for i in answer:
    print(i)
