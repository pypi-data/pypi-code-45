import os

import time

exelist = ['copy_time.exe','IEOpen.exe','runoffice.exe','unzip_time.exe']

path = os.getcwd()+ '\\'


time.sleep(360)
starttime = time.time()

while True:
    for exe in exelist:
        try:
            os.system(path+ exe)
            time.sleep(600)
        except Exception,ex:
            print ex  
    time.sleep(5400)
    if time.time() - starttime > 86400:
        break
print 'over'
    
    
    
    

        

