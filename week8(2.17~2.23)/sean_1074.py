N, r, c = map(int, input().split())

count = 0


def z_moving(x, y, size):
    global count

    if x == r and y == c:
        print(count)
        exit(0)

    if size == 1:
        count += 1
        return

    if not(x <= r < x+size) or not(y <= c < y+size):
        count += size ** 2
        return

    z_moving(x, y, size // 2)
    z_moving(x, y + size // 2, size // 2)
    z_moving(x + size // 2, y, size // 2)
    z_moving(x + size // 2, y + size // 2, size // 2)


z_moving(0, 0, 2**N)
