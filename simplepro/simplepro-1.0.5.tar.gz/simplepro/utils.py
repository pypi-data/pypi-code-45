import json 
from django .core .serializers .json import DjangoJSONEncoder 
from django .db .models import ForeignKey 
from django .http import HttpResponse 
from django .utils .encoding import force_text 
from django .utils .functional import Promise 
import datetime 
class LazyEncoder (DjangoJSONEncoder ):
    ""
    def default (self ,obj ):
        if isinstance (obj ,datetime .datetime ):
            return obj .strftime ("%Y-%m-%d %H:%M:%S")
        elif isinstance (obj ,datetime .date ):
            return obj .strftime ("%Y-%m-%d")
        elif isinstance (obj ,Promise ):
            return force_text (obj )
        return str (obj )
def get_model_fields (model ,O00O0000O000OOOOO =None ):
    ""
    OO0O0OO0O0000000O =[]
    OOO0O0O000O0OO000 =model ._meta .fields 
    for O0OOOOOOO0000O0OO in OOO0O0O000O0OO000 :
        OOOOO0O000O0OO000 =O0OOOOOOO0000O0OO .name 
        if hasattr (O0OOOOOOO0000O0OO ,'verbose_name'):
            OOOOO0O000O0OO000 =getattr (O0OOOOOOO0000O0OO ,'verbose_name')
        if isinstance (OOOOO0O000O0OO000 ,Promise ):
            OOOOO0O000O0OO000 =str (OOOOO0O000O0OO000 )
        if O00O0000O000OOOOO :
            OO0O0OO0O0000000O .append (('{}__{}'.format (O00O0000O000OOOOO ,O0OOOOOOO0000O0OO .name ),OOOOO0O000O0OO000 ))
        else :
            OO0O0OO0O0000000O .append ((O0OOOOOOO0000O0OO .name ,OOOOO0O000O0OO000 ))
    return OO0O0OO0O0000000O 
def find_field (fields ,name ):
    for O000OOOOO0O0OO0OO in fields :
        if name ==O000OOOOO0O0OO0OO [0 ]:
            return O000OOOOO0O0OO0OO [1 ]
    return False 
MODEL_CACHE ={}
def get_model_info (model_admin ,request ):
    OO0O0O00000OO0O0O =str (model_admin )
    if OO0O0O00000OO0O0O in MODEL_CACHE :
        O0O0OO0O0OOOO00O0 =MODEL_CACHE .get (OO0O0O00000OO0O0O )
        return O0O0OO0O0OOOO00O0 .get ('values_fields'),O0O0OO0O0OOOO00O0 .get ('fun_fields'),O0O0OO0O0OOOO00O0 .get ('headers'),O0O0OO0O0OOOO00O0 .get ('formatter'),O0O0OO0O0OOOO00O0 .get ('choices')
    OOOO0OOO0OO000OO0 =get_model_fields (model_admin .model )
    OO0OOOO0000OOOO0O =model_admin .get_list_display (request )
    O0OOO0O00OOO0OOO0 =[]
    OO0000O000OO0O0OO =[]
    O0OOOO0OOO000OO0O =[]
    O0OO000OO000OOOOO ={}
    if hasattr (model_admin ,'fields_options'):
        O0OO000OO000OOOOO =getattr (model_admin ,'fields_options')
    for OOOOO0O0OOO0OO00O in OO0OOOO0000OOOO0O :
        OO00O0000OO0000OO =find_field (OOOO0OOO0OO000OO0 ,OOOOO0O0OOO0OO00O )
        if OO00O0000OO0000OO :
            OO0000O000OO0O0OO .append (OOOOO0O0OOO0OO00O )
            OO0OO0OO000OO0OO0 ={'name':OOOOO0O0OOO0OO00O ,'label':OO00O0000OO0000OO }
            if OOOOO0O0OOO0OO00O in O0OO000OO000OOOOO :
                OO0OO0OO000OO0OO0 =dict (OO0OO0OO000OO0OO0 ,**O0OO000OO000OOOOO .get (OOOOO0O0OOO0OO00O ))
            if 'sortable'not in OO0OO0OO000OO0OO0 :
                OO0OO0OO000OO0OO0 ['sortable']='custom'
            O0OOOO0OOO000OO0O .append (OO0OO0OO000OO0OO0 )
        else :
            O0OOO0O00OOO0OOO0 .append (OOOOO0O0OOO0OO00O )
            OO00O0000OO0000OO =OOOOO0O0OOO0OO00O 
            if hasattr (model_admin ,OOOOO0O0OOO0OO00O ):
                OO0OOO0O0O0O0O0O0 =getattr (model_admin ,OOOOO0O0OOO0OO00O ).__dict__ 
            else :
                OO0OOO0O0O0O0O0O0 =getattr (model_admin .model ,OOOOO0O0OOO0OO00O ).__dict__ 
            if 'short_description'in OO0OOO0O0O0O0O0O0 :
                OO00O0000OO0000OO =OO0OOO0O0O0O0O0O0 .get ('short_description')
            elif OO00O0000OO0000OO =='__str__':
                OO00O0000OO0000OO =model_admin .model ._meta .verbose_name_plural 
            OO0OO0OO000OO0OO0 ={'name':OOOOO0O0OOO0OO00O ,'label':OO00O0000OO0000OO }
            if OOOOO0O0OOO0OO00O in O0OO000OO000OOOOO :
                OO0OO0OO000OO0OO0 =dict (OO0OO0OO000OO0OO0 ,**O0OO000OO000OOOOO .get (OOOOO0O0OOO0OO00O ))
            OO0OO0OO000OO0OO0 ['sortable']=False 
            O0OOOO0OOO000OO0O .append (OO0OO0OO000OO0OO0 )
    OOOOOOO0OOO0OO0OO =None 
    if hasattr (model_admin ,'formatter'):
        OOOOOOO0OOO0OO0OO =getattr (model_admin ,'formatter')
    O0000O00OO0O000O0 =model_admin .model 
    OO00O0000OOO00OOO ={}
    for O0O00OOOO000O00OO in dir (O0000O00OO0O000O0 ):
        if O0O00OOOO000O00OO .endswith ('choices'):
            OOO00OO0OO00O0000 ={}
            OO00OO0OO0OOO0000 =getattr (O0000O00OO0O000O0 ,O0O00OOOO000O00OO )
            for OOOOO0O0OOO0OO00O in OO00OO0OO0OOO0000 :
                OOO00OO0OO00O0000 [OOOOO0O0OOO0OO00O [0 ]]=OOOOO0O0OOO0OO00O [1 ]
            OO00O0000OOO00OOO [O0O00OOOO000O00OO ]=OOO00OO0OO00O0000 
    for O0O00OOOO000O00OO in O0000O00OO0O000O0 ._meta .fields :
        OOO00OO0OO00O0000 ={}
        if hasattr (O0O00OOOO000O00OO ,'choices'):
            if len (O0O00OOOO000O00OO .choices )>0 :
                for OOOOO0O0OOO0OO00O in O0O00OOOO000O00OO .choices :
                    OOO00OO0OO00O0000 [OOOOO0O0OOO0OO00O [0 ]]=OOOOO0O0OOO0OO00O [1 ]
                OO00O0000OOO00OOO [O0O00OOOO000O00OO .name ]=OOO00OO0OO00O0000 
    MODEL_CACHE [OO0O0O00000OO0O0O ]={'values_fields':OO0000O000OO0O0OO ,'fun_fields':O0OOO0O00OOO0OOO0 ,'headers':O0OOOO0OOO000OO0O ,'formatter':OOOOOOO0OOO0OO0OO ,'choices':OO00O0000OOO00OOO ,}
    return OO0000O000OO0O0OO ,O0OOO0O00OOO0OOO0 ,O0OOOO0OOO000OO0O ,OOOOOOO0OOO0OO0OO ,OO00O0000OOO00OOO 
def get_custom_button (request ,admin ):
    OO0000OOOOO0O000O ={}
    OOOOOO00000O0O0O0 =admin .get_actions (request )
    O00O0O0O0O000OOO0 =admin .opts .app_label 
    if OOOOOO00000O0O0O0 :
        OO000OOOO0000O0O0 =0 
        for OO00OO00OOO0OO0O0 in OOOOOO00000O0O0O0 :
            O0OOO00OOOO00OOO0 ={}
            OOOOO00OOOOOOOOO0 =OOOOOO00000O0O0O0 .get (OO00OO00OOO0OO0O0 )[0 ]
            for OO0O0OO0OOO0OO0O0 ,O0O00OOO0OOO0OOO0 in OOOOO00OOOOOOOOO0 .__dict__ .items ():
                if OO0O0OO0OOO0OO0O0 !='__len__'and OO0O0OO0OOO0OO0O0 !='__wrapped__':
                    O0OOO00OOOO00OOO0 [OO0O0OO0OOO0OO0O0 ]=O0O00OOO0OOO0OOO0 
            O0OOO00OOOO00OOO0 ['eid']=OO000OOOO0000O0O0 
            OO000OOOO0000O0O0 +=1 
            if OO00OO00OOO0OO0O0 =='export_admin_action':
                O0OOO00OOOO00OOO0 ['label']='选中导出'
                O0OOO00OOOO00OOO0 ['isExport']=True 
                O0OOO00OOOO00OOO0 ['icon']='el-icon-finished'
                OO0OO0OO00000OOOO =[]
                for O0O00O0O0O000OO00 in enumerate (admin .get_export_formats ()):
                    OO0OO0OO00000OOOO .append ({'value':O0O00O0O0O000OO00 [0 ],'label':O0O00O0O0O000OO00 [1 ]().get_title ()})
                O0OOO00OOOO00OOO0 ['formats']=OO0OO0OO00000OOOO 
            else :
                O0OOO00OOOO00OOO0 ['label']=OOOOOO00000O0O0O0 .get (OO00OO00OOO0OO0O0 )[2 ]
            if request .user .has_perm ('{}.{}'.format (O00O0O0O0O000OOO0 ,OO00OO00OOO0OO0O0 )):
                OO0000OOOOO0O000O [OO00OO00OOO0OO0O0 ]=O0OOO00OOOO00OOO0 
    if 'delete_selected'in OO0000OOOOO0O000O :
        del OO0000OOOOO0O000O ['delete_selected']
    return OO0000OOOOO0O000O 
def search_placeholder (cl ):
    O000O000000OOOO0O =get_model_fields (cl .model )
    for O00OO00O00000OO0O in cl .model ._meta .fields :
        if isinstance (O00OO00O00000OO0O ,ForeignKey ):
            O000O000000OOOO0O .extend (get_model_fields (O00OO00O00000OO0O .related_model ,O00OO00O00000OO0O .name ))
    O00O0OO00000OOOOO =[]
    for OOOOOOOO000000OO0 in cl .search_fields :
        for O00OO00O00000OO0O in O000O000000OOOO0O :
            if O00OO00O00000OO0O [0 ]==OOOOOOOO000000OO0 :
                O00O0OO00000OOOOO .append (O00OO00O00000OO0O [1 ])
                break 
    return ",".join (O00O0OO00000OOOOO )
def write (data ,O0O00OO00OO00OO0O ='ok',O000O0O0OO00OO0OO =True ):
    OO00OO0OOO0O0OO0O ={'state':O000O0O0OO00OO0OO ,'msg':O0O00OO00OO00OO0O ,'data':data }
    return HttpResponse (json .dumps (OO00OO0OOO0O0OO0O ,cls =LazyEncoder ),content_type ='application/json')
def write_obj (obj ):
    return HttpResponse (json .dumps (obj ,cls =LazyEncoder ),content_type ='application/json')
def has_permission (request ,admin ,permission ):
    O0OOOO0O0OOO00O0O =get_permission_codename (permission ,admin .opts )
    OOOO0OO0O0O00O0OO ='{}.{}'.format (admin .opts .app_label ,O0OOOO0O0OOO00O0O )
    return request .user .has_perm (OOOO0OO0O0O00O0OO )
def get_permission_codename (action ,opts ):
    ""
    return '%s_%s'%(action ,opts .model_name )
from simpleui .templatetags import simpletags 
from simpleui .templatetags .simpletags import get_config 
def get_menus (request ,admin_site ):
    ""
    O0OOOO0OOO0O0000O ={'app_list':admin_site .get_app_list (request ),'request':request }
    def O0OO0O00O0OOOO00O (key ):
        return request .user .has_perm (key )
    def _O0O0OO0OOO00O0OO0 (key ):
        if key =='SIMPLEUI_CONFIG':
            _OOOOOO00OOOO0OOO0 =get_config (key )
            if _OOOOOO00OOOO0OOO0 and 'menus'in _OOOOOO00OOOO0OOO0 :
                OO000O00O0OO0OOO0 =_OOOOOO00OOOO0OOO0 .get ('menus')
                OO00O0OOO0OO0O00O =[]
                for OOOOOO0O0O0OOOOOO in OO000O00O0OO0OOO0 :
                    if 'codename'not in OOOOOO0O0O0OOOOOO :
                        OO00O0OOO0OO0O00O .append (OOOOOO0O0O0OOOOOO )
                        continue 
                    OO0OO00O0OOOOOO0O =OOOOOO0O0O0OOOOOO .get ('codename')
                    key ='{}.{}'.format (OO0OO00O0OOOOOO0O ,OO0OO00O0OOOOOO0O )
                    if O0OO0O00O0OOOO00O (key ):
                        if 'models'in OOOOOO0O0O0OOOOOO :
                            OOO00O0OO00O00OO0 =OOOOOO0O0O0OOOOOO .get ('models')
                            O0O0O00OOOO0OO0O0 =[]
                            for O0O0000O00OOO00O0 in OOO00O0OO00O00OO0 :
                                if 'codename'in O0O0000O00OOO00O0 :
                                    if O0OO0O00O0OOOO00O ('{}.{}'.format (OO0OO00O0OOOOOO0O ,O0O0000O00OOO00O0 .get ('codename'))):
                                        O0O0O00OOOO0OO0O0 .append (O0O0000O00OOO00O0 )
                                else :
                                    O0O0O00OOOO0OO0O0 .append (O0O0000O00OOO00O0 )
                            OOOOOO0O0O0OOOOOO ['models']=O0O0O00OOOO0OO0O0 
                        OO00O0OOO0OO0O00O .append (OOOOOO0O0O0OOOOOO )
                _OOOOOO00OOOO0OOO0 ['menus']=OO00O0OOO0OO0O00O 
        return _OOOOOO00OOOO0OOO0 
    return simpletags .menus (O0OOOO0OOO0O0000O ,_get_config =_O0O0OO0OOO00O0OO0 )
