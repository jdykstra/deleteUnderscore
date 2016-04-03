import errno, os, stat, sys, subprocess
import argparse

""" 
Delete underscores in camera image filenames within current working directory.

Usage:
python deleteUnderscore.py  --remove-underscores [directory]
"""
version = "0.1"

global args

#  Process all files in one directory."
def doOneDirectory(dirpath, filenames):
    dirpath = dirpath
    for leaf in filenames:
        doOneFile(dirpath, leaf)

# Do the requested processing on one file"
def doOneFile(dirpath, filename):
    #  Only touch image files beginning in an underscore or a C."
    name, ext = os.path.splitext(filename)
    if not ext.lower() in {".nef", ".jpg", ".jpeg", ".tif", ".tiff", ".xmp"}:
        return
    if name[0] not in {"_", "C"}:
        return
    
    if args.progress:
        print filename
        
    #  Delete underscores.  Allow silent deletions if a file with the name already exists."
    if args.delete_underscores:
        os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, filename.replace("_", "")))


def main():    
    global args
    
    parser = argparse.ArgumentParser(description="Manage camera image files")
    parser.add_argument("--recursive", action="store_true", help="Recurse into subdirectories.")
    parser.add_argument("--delete-underscores", action="store_true", help="Remove underscores in filenames.")
    parser.add_argument("--run", help="Name of program to run, with target directory as its parameter.")
    parser.add_argument('--progress', action='store_true', help="Print what is done to each file.")
    parser.add_argument('--version', action='version', version='%(prog)s ' + version)
    parser.add_argument("dir", nargs='?', default=os.getcwd(), help="Directory containing files;  Use the working directory if not specified.")
    args = parser.parse_args()
    
    if args.recursive:
        dirs = os.walk(args.dir)
        for dir in dirs:
            doOneDirectory(dir[0], dir[2])
    else:
            doOneDirectory(args.dir, os.listdir(args.dir))
    
    #  Now run the external program, if specified.  Because this passes the start command"
    #  to the OS shell, it is Windows-specific."
    if args.run != None:
        os.system("start \"\" \""+args.run +"\" \""+args.dir+"\"")
            
if __name__ == '__main__':
    main()
