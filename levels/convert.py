import pickle, shutil

EMPTY = 0
WALL = 1
BOX = 2
STORAGE = 3
PLAYER = 4
STOBOX = 5

import os

for levelset in [os.path.splitext(s)[0] for s in
                 filter(lambda s: os.path.splitext(s)[1] == '.txt',
                       os.listdir("."))]:
    if not os.path.exists("%s"%levelset):
        os.mkdir("%s"%levelset)

    levels = open("%s.txt"%levelset, "r").read().split("\n\n")
    lv = []
    for level in levels:
        try:
            lines = level.split("\n")
            name = lines[0]
            lvl = []
            w = 0
            for line in lines[1:]:
                if line[0] == ';':
                    continue
                if line[0] == "'":
                    name = line.split("'")[1]
                    continue
                lvl.append([])
                cnt = 0
                for c in line:
                    cnt += 1
                    lvl[-1].append(" #$.@*+".index(c))
                w = max(w, cnt)
            for row in lvl:
                for i in range(w-len(row)):
                    row.append(EMPTY)
            pickle.dump(lvl, open("%s/%s.ppl"%(levelset, name), "wb"))
        except:
            pass
        else:
            lv.append(name)
    pickle.dump(lv, open("%s.ppo"%levelset, "wb"))

