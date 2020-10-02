def dblLinear(n):
    u, x, y = [1], 0, 0
    for i in range(n):
        nextX, nextY = 2*u[x]+1, 3*u[y]+1
        if nextX <= nextY:
            u.append(nextX)
            x += 1
            if nextX == nextY:
                y += 1
        else:
            u.append(nextY)
            y += 1
    return u[n]
