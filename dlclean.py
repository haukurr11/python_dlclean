import re
import os
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
            
        except:
            continue
            
    
