
##    PushPush v1.0
##
##    Copyright (C) 2011 kuviman
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##    you can contact me kuviman@gmail.com

import pickle, shutil, os

name = raw_input("name: ")
levels = raw_input("levels to include: ").split()

pickle.dump(levels, open('%s.ppo'%name, 'wb'))
if not os.path.isdir(name):
    os.mkdir(name)
for level in levels:
    shutil.move("user levels/%s.ppl"%level,
                "%s/%s.ppl"%(name,level))
