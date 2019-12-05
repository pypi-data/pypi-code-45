from .import handlers as handlers 
try :
    from django .utils .deprecation import MiddlewareMixin 
except ImportError :
    MiddlewareMixin =object 
import os 
class SimpleMiddleware (MiddlewareMixin ):
    def process_request (self ,request ):
        OOO0000OO00O0OOO0 =os .environ .get ('sp_is_ready')
        if not OOO0000OO00O0OOO0 :
            os .environ .setdefault ('sp_is_ready','True')
            from .import urls 
            urls .init ()
        O0OOO0O0O0OOOOOOO =request .path 
        if not O0OOO0O0O0OOOOOOO .endswith ('/'):
            O0OOO0O0O0OOOOOOO =O0OOO0O0O0OOOOOOO +'/'
        return handlers .process_request (request ,O0OOO0O0O0OOOOOOO )
    def process_view (self ,request ,view_func ,view_args ,view_kwargs ):
        return handlers .process_view (request ,view_func )
    def process_response (self ,request ,response ):
        handlers .done (request )
        return response 
