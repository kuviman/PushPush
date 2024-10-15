
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

from ppgame.constants import *

script = 'PushPush.py'
srcpath = '%s_%s_src'%(TITLE, VERSION)
exe_path = '%s_%s_win32'%(TITLE, VERSION)
data = ['data', 'levels']

pythondll = 'C:/python26/python26.dll'

gplcomment = '''
##    %s
##
##    %s
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

''' % (FULL_TITLE, COPYRIGHT)

import py2exe, shutil, sys, os
from  distutils.core import setup
from zipfile import ZipFile

shutil.copytree('.', srcpath,
                ignore=shutil.ignore_patterns(
                    '*.pyc', '*.pp', 'error.txt', 'log.txt', 'downloaded', '*.zip'))
z = ZipFile(srcpath+'.zip', 'w')
for root, dirs, files in os.walk(srcpath):
    for name in files:
        path = os.path.join(root, name)
        if os.path.splitext(name)[1] == '.py':
            text = open(path).read()
            f = open(path, 'w')
            f.write(gplcomment)
            f.write(text)
            f.close()
        z.write(path)
z.close()

shutil.rmtree(srcpath)

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll",
                                              "libogg-0.dll",
                                              "sdl_ttf.dll"):
        return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL
sys.argv.append('py2exe')
setup(windows=[script],
      options={'py2exe': {
          'bundle_files': 1,
          'excludes': ['OpenGL']}},
      )#    data_files=data)

print('adding OpenGL to library.zip...')
ZipFile('dist/library.zip', 'r').extractall("lib")
shutil.copytree('C:/python26/lib/site-packages/OpenGL', 'lib/OpenGL')
f = ZipFile('dist/library.zip', 'w')
for root, dirs, files in os.walk('lib'):
    for name in files:
        f.write(os.path.join(root, name), os.path.join(root[4:], name))
f.close()

shutil.copy(pythondll, 'dist')
shutil.rmtree('lib')
shutil.rmtree('build')
for d in data:
    shutil.copytree(d, 'dist/'+d)
os.rename('dist', exe_path)
print('making win32 zip')
f = ZipFile(exe_path+'.zip', 'w')
for root, dirs, files in os.walk(exe_path):
    for name in files:
        f.write(os.path.join(root, name))
f.close()
shutil.rmtree(exe_path)

py2exe.build_exe.isSystemDLL = origIsSystemDLL
