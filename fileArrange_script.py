import os
import shutil
for a in os.listdir(os.getcwd()):
    if os.path.isfile(a):
        b=a.split('.')[-1]
        if not os.path.exists(b):
            os.mkdir(b)
        try:
            shutil.move(a,b)
        except:
            pass
        