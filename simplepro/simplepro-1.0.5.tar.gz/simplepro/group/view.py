import os 
from django .contrib .auth .models import Group 
from django .views .decorators .csrf import csrf_exempt 
from simplepro .utils import write 
from .utils import get_permissions 
import base64 
def action (request ):
    OO0O0O00OOOO0OOOO =request .POST .get ('action')
    O000O00OO0000O0OO ={'tree':get_tree ,'save':save ,'get_detail':get_detail }
    return O000O00OO0000O0OO .get (OO0O0O00OOOO0OOOO )(request )
def get_detail (request ):
    O0O00OOO0O0O0O00O =request .POST .get ('id')
    O00O0OOO00O0OOO00 =Group .objects .filter (id =O0O00OOO0O0O0O00O ).first ()
    O0O00000OOO0O00OO =[]
    if O00O0OOO00O0OOO00 :
        O0O0OOO0OO0OO0O0O =O00O0OOO00O0OOO00 .permissions .all ()
        for O0O0OO00O0OOOOOOO in O0O0OOO0OO0OO0O0O :
            O0O00000OOO0O00OO .append (O0O0OO00O0OOOOOOO .id )
    return write (O0O00000OOO0O00OO )
def save (request ):
    OOO000O0OO0O00O0O =True 
    O0O0O0000O0OOO0OO ="ok"
    try :
        OO00000O0O000OO0O =request .POST .get ('name')
        O0O0O0OOOOOOO000O =request .POST .get ('ids')
        O00OOO00OOO0OOOOO =request .POST .get ('id')
        if O00OOO00OOO0OOOOO and O00OOO00OOO0OOOOO !='':
            O0O00O0OO0OOOO0O0 =Group .objects .get (id =O00OOO00OOO0OOOOO )
            O0O00O0OO0OOOO0O0 .permissions .clear ()
        else :
            O0O00O0OO0OOOO0O0 =Group .objects .create (name =OO00000O0O000OO0O )
        if O0O0O0OOOOOOO000O and O0O0O0OOOOOOO000O !='':
            O0O0O0OOOOOOO000O =O0O0O0OOOOOOO000O .split (',')
            for OO0OO00OOOOOO0O0O in O0O0O0OOOOOOO000O :
                O0O00O0OO0OOOO0O0 .permissions .add (OO0OO00OOOOOO0O0O )
    except Exception as O00OOO0000OO000OO :
        OOO000O0OO0O00O0O =False 
        O0O0O0000O0OOO0OO =O00OOO0000OO000OO .args [0 ]
    return write (None ,O0O0O0000O0OOO0OO ,OOO000O0OO0O00O0O )
def get_tree (request ):
    ""
    O0O0000O0O0OOOO0O =get_permissions ()
    return write (O0O0000O0O0OOOO0O )
@csrf_exempt 
def offline_active (request ):
    OOO00O000000OOO00 =True 
    OOOOO0OOO00OOOOO0 ='激活文件写入成功！'
    try :
        OO0OOO0000O0O00OO =os .path .join (os .getcwd (),'simplepro.lic')
        O00OO0O0OO000OO00 =open (OO0OOO0000O0O00OO ,'wb')
        O00OO0O0OO000OO00 .seek (0 )
        O00OO0O00O00O0OO0 =request .POST .get ('code')
        OO0OOO0OOOO0O0O00 =base64 .b64decode (O00OO0O00O00O0OO0 )
        O00OO0O0OO000OO00 .write (OO0OOO0OOOO0O0O00 )
        O00OO0O0OO000OO00 .close ()
        request .reload =True 
    except Exception as O0O0OO0000OO0OOOO :
        OOO00O000000OOO00 =False 
        OOOOO0OOO00OOOOO0 =O0O0OO0000OO0OOOO .args [0 ]
    return write (None ,OOOOO0OOO00OOOOO0 ,OOO00O000000OOO00 )
