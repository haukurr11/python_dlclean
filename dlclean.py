import re
import os
import shutil
def dlclean(source,target,search):
    files = [ name for name in os.listdir(source)
    if os.path.isfile(os.path.join(source, name))
    and search.lower() in name.replace('.', ' ').lower()]
    for x in files:
        try:
            regEx = re.search("s(\d\d)e(\d\d)", x)
            season = int(regEx.group(1))
            episode = int(regEx.group(2))
            print(season, episode)
            targetPath = target+"\\"+search
            fullPath = targetPath+"\\"+"Season "+str(season)
            try:
                os.mkdir(targetPath)
            except FileExistsError:
                pass
            try:
                os.mkdir(fullPath)
            except FileExistsError:
                pass
            sour = source+"\\"+x
            shutil.copyfile(sour, fullPath+"\\"+x)
        except AttributeError:
            continue
            
    
