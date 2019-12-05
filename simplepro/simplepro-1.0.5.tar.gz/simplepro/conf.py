import uuid 
import sys 
import os 
def get_server_url ():
    return 'https://simpleui.88cto.com'
_O00000O0O0OOOOO00 =None 
def get_device_id ():
    global _O00000O0O0OOOOO00 
    if _O00000O0O0OOOOO00 :
        return _O00000O0O0OOOOO00 
    _O00000O0O0OOOOO00 =_O00O00000O000OOO0 ()
    return _O00000O0O0OOOOO00 
def _O00O00000O000OOO0 ():
    OOO0O0OOOOOOOO00O =uuid .getnode ()
    try :
        if sys .platform =='darwin':
            OOO0O0OOOOOOOO00O =os .popen ("system_profiler SPHardwareDataType | fgrep 'UUID' | awk '{print $NF}'").read ()
        if sys .platform =='win32':
            import wmi 
            OO0000OOOO000O0O0 =wmi .WMI ()
            OOO0O0OOOOOOOO00O =OO0000OOOO000O0O0 .Win32_BaseBoard ()[0 ].SerialNumber .strip ()
        elif sys .platform =='linux':
            OOO0O0OOOOOOOO00O =os .popen ('cat /sys/class/dmi/id/product_uuid').read ()
        OOO0O0OOOOOOOO00O =OOO0O0OOOOOOOO00O .strip ()
        OOO0O0OOOOOOOO00O =str (OOO0O0OOOOOOOO00O ).replace ('-','')
        if len (OOO0O0OOOOOOOO00O )==32 :
            O0O00000O0OO00OOO =[]
            for OO0O00OOO0O0OO0OO in range (0 ,8 ):
                O0O00000O0OO00OOO .append (OOO0O0OOOOOOOO00O [OO0O00OOO0O0OO0OO *4 ])
            OOO0O0OOOOOOOO00O ="".join (O0O00000O0OO00OOO )
    except Exception as O00O0O0OOOO00O0OO :
        print ('Waring! Unable to get device ID')
        print (O00O0O0OOOO00O0OO )
    return OOO0O0OOOOOOOO00O 
if __name__ =='__main__':
    print (_O00O00000O000OOO0 ())
