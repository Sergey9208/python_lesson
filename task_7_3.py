from os import path, walk, listdir
import shutil

name = 'my_project'

try:
    for root, dirs, files in walk(name):
        if 'templates' in dirs and root != name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry), path.join(name, 'templates', entry))
except FileExistsError:
    print("Templates already to work")