import json 
from django import template 
register =template .Library ()
from import_export .admin import ImportExportMixinBase 
from simplepro import conf 
import simplepro 
import simpleui 
@register .simple_tag (takes_context =True )
def has_import_export (context ):
    O0000OO00O0O00O0O =context .get ('cl')
    return issubclass (O0000OO00O0O00O0O .__class__ ,ImportExportMixinBase )
@register .simple_tag (takes_context =True )
def get_display_name (context ):
    OO0O0OO0O0OO0OO00 =context .get ('user')
    if OO0O0OO0O0OO0OO00 :
        OOOO0OO00OO0OO0O0 =''
        if OO0O0OO0O0OO0OO00 .first_name :
            OOOO0OO00OO0OO0O0 +=OO0O0OO0O0OO0OO00 .first_name 
        if OO0O0OO0O0OO0OO00 .last_name :
            OOOO0OO00OO0OO0O0 +=OO0O0OO0O0OO0OO00 .last_name 
    if not OOOO0OO00OO0OO0O0 :
        OOOO0OO00OO0OO0O0 =str (OO0O0OO0O0OO0OO00 )
    return OOOO0OO00OO0OO0O0 
@register .simple_tag 
def get_server_url ():
    return conf .get_server_url ()
@register .simple_tag 
def get_sp_version ():
    return simplepro .get_version ()
@register .simple_tag 
def get_device_id ():
    return conf .get_device_id ()
@register .simple_tag 
def get_simple_version ():
    return simpleui .get_version ()
@register .simple_tag (takes_context =True )
def test_tag (context ):
    print (context )
    O0O0OO0O0OO00OO00 =context .get ('fieldset')
    for O0OO0OOOO0O0OOOOO in O0O0OO0O0OO00OO00 :
        print (O0OO0OOOO0O0OOOOO )
    pass 
