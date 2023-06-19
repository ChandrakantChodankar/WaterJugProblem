x = int(input("capacity of jug A: "))
y = int(input("capacity of jug B: "))
z = int(input("capacity of jug C: "))
initial_state = (8, 0, 0)
visited = {}
path = []
goala = int(input("final capacity of jug A: "))
goalb = int(input("final capacity of jug B: "))


def waterjugstate(state):
    a = state[0]
    b = state[1]
    c = state[2]
    if (a == goala and b == goalb):
        path.append(state)
        return True
    if (a, b, c) in visited:
        return False
    visited[a, b, c] = 1

    if (a > 0):
        if (a+b <= y):
            if (waterjugstate((0, a+b, c))):
                path.append(state)
                return True
        else:
            if (waterjugstate((a-(y-b), y, c))):
                path.append(state)
                return True

        if (a+c <= z):
            if (waterjugstate((0, b, a+c))):
                path.append(state)
                return True
            else:
                if (waterjugstate((a-(z-c), b, z))):
                    path.append(state)
                    return True

    if (b > 0):
        if (a+b <= x):
            if (waterjugstate((a+b, 0, c))):
                path.append(state)
                return True
        else:
            if (waterjugstate((x, b-(x-a), c))):
                path.append(state)
                return True

        if (b+c <= z):
            if (waterjugstate((a, 0, b+c))):
                path.append(state)
                return True
        else:
            if (waterjugstate((a, b-(z-c), z))):
                path.append(state)
                return True

    if (c > 0):
        if (a+c <= x):
            if (waterjugstate((a+c, b, 0))):
                path.append(state)
                return True
        else:
            if (waterjugstate((x, b, c-(x-a)))):
                path.append(state)
                return True

        if (b+c <= y):
            if (waterjugstate((a, b+c, 0))):
                path.append(state)
                return True
        else:
            if (waterjugstate((a, y, c-(y-b)))):
                path.append(state)
                return True

    return False


waterjugstate(initial_state)
path.reverse()
for i in path:
    print(i)
