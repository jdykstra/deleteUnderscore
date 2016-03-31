import os

""" 
Delete underscores in filenames within current working directory.

Usage:
python deleteUnderscore.py
"""

path =  os.getcwd()

dirs = os.walk(path)
for dir in dirs:
    dirpath = dir[0]
    for leaf in dir[2]:
        if leaf[0] not in {"_", "C"}:
            continue
        filename = os.path.join(dirpath, leaf)
        print filename
        os.rename(filename, filename.replace("_", ""))
