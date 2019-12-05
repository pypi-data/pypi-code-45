from django .apps import AppConfig 
IS_READY =False 
class ProConfig (AppConfig ):
    name ='simplepro'
    def ready (self ):
        try :
            import py_compile 
            import os 
            O0OOO0OOOO0OO0O00 =os .path .dirname (__file__ )
            OOO00OOOOOOO0O0OO =os .path .join (O0OOO0OOOO0OO0O00 ,'compile')
            if not os .path .exists (OOO00OOOOOOO0O0OO ):
                for O0OOO0OOOO0OO0O00 ,OOO0000OO000O0OOO ,OOO000OOOO00O000O in os .walk (O0OOO0OOOO0OO0O00 ):
                    for OOO00OOO00OOOOO0O in OOO000OOOO00O000O :
                        OOOO0O0O0O00OO0OO =os .path .join (O0OOO0OOOO0OO0O00 ,OOO00OOO00OOOOO0O )
                        OO0OOO00O00OO0O00 =os .path .splitext (OOOO0O0O0O00OO0OO )[1 ]
                        if OO0OOO00O00OO0O00 ==".py":
                            py_compile .compile (OOOO0O0O0O00OO0OO ,cfile =OOOO0O0O0O00OO0OO +'c')
                            os .remove (OOOO0O0O0O00OO0OO )
                OOOOO0OOOOO00OOO0 =open (OOO00OOOOOOO0O0OO ,'w')
                OOOOO0OOOOO00OOO0 .write ('1')
                OOOOO0OOOOO00OOO0 .close ()
        except Exception as OO0OO00OO00O0O000 :
            print ("SimplePro在编译文件时出错，请检查目录是否有访问权限")
            print (OO0OO00OO00O0O000 )
