from random import *
import pickle

EMPTY = 0
WALL = 1
BOX = 2
STORAGE = 3
PLAYER = 4
STOBOX = 5
PLASTO = 6

def main():
    symbols = ' #$.@*+?'
    maxstep = 5
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    k = input("steps in solution: ")
    m = [[-1]*100 for i in range(100)]
    x, y = 50, 50
    ld = -1
    for i in range(k):
        nd = randrange(4)
        while nd == ld:
            nd = randrange(4)
        ld = nd
        dx, dy = d[nd]
        bf = choice([True, False])
        if bf:
            m[x-dx][y-dy] = STORAGE
        steps = randrange(1, maxstep)
        box = randrange(steps) if bf else -1
        for j in range(steps):
            if j == box:
                #print("box added")
                m[x][y] = BOX
            x += dx; y += dy
            m[x][y] = EMPTY
    m[x][y] = PLAYER
    m3 = []
    for i in range(100):
        m3.append([])
        for j in range(100):
            m3[-1].append(m[i][j])
    for i in range(1, 99):
        for j in range(1, 99):
            if m[i][j] != -1:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if m[i+dx][j+dy] == -1:
                            m3[i+dx][j+dy] = WALL
    fi = fj = 100
    for i in range(100):
        for j in range(100):
            if m3[i][j] != -1:
                fi = min(fi, i)
                li = i
    for j in range(100):
        for i in range(100):
            if m3[i][j] != -1:
                fj = min(fj, j)
                lj = j
    m2 = []
    for i in range(fi, li+1):
        m2.append([])
        s = ''
        for j in range(fj, lj+1):
            if m3[i][j] == -1:
                m3[i][j] = 0
            m2[-1].append(m3[i][j])
            #s += str(m3[i][j])
            s += symbols[m3[i][j]]
        print(s)
    name = raw_input('name: ')
    pickle.dump(m2, open('generated/%s.ppl'%name, 'wb'))

main()
