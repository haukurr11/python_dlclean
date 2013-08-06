import re
import os
import shutil
import sys

"""
organizes tv shows in a given directory
recognizes the pattern sXXeX
where s stands for season and e for episode
source: source directory
target: target directory
search: name of tv show
"""
def dlclean(source,target,search):
    filenames = [ name for name in os.listdir(source)
                  if os.path.isfile(os.path.join(source, name))
                  and search.lower() in name.replace('.', ' ').lower()]
    dirs = [ name for name in os.listdir(source)
             if os.path.isdir(os.path.join(source, name))]
    for d in dirs:
        dlclean(source + "/" + d,target,search)
    for filename in filenames:
        try:
            regEx = re.search("s(\d\d)e(\d\d)", filename)
            season = int(regEx.group(1))
            targetPath = target+"/"+search
            fullPath = targetPath+"/"+"Season "+str(season)
            try:
                os.mkdir(targetPath)
            except OSError:
                pass
            try:
                os.mkdir(fullPath)
            except OSError:
                pass
            sour = source+"/"+filename
            print(fullPath)
            shutil.copyfile(sour, fullPath+"/"+filename)
        except AttributeError:
            continue

def main():
   dlclean(sys.argv[1],sys.argv[2],sys.argv[3])


if __name__ == '__main__':
    main()
