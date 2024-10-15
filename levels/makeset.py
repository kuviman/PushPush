import pickle, shutil, os

name = raw_input("name: ")
levels = raw_input("levels to include: ").split()

pickle.dump(levels, open('%s.ppo'%name, 'wb'))
if not os.path.isdir(name):
    os.mkdir(name)
for level in levels:
    shutil.move("user levels/%s.ppl"%level,
                "%s/%s.ppl"%(name,level))
