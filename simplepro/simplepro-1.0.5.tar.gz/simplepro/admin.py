from django .contrib .admin .models import LogEntry 
from django .contrib .auth .admin import GroupAdmin 
from django .contrib import admin 
from django .contrib .auth .models import Permission 
from django .contrib .contenttypes .models import ContentType 
@admin .register (ContentType )
class ContentTypeAdmin (admin .ModelAdmin ):
    list_display =('id','app_label','model')
    list_per_page =20 
    search_fields =('app_label','model')
@admin .register (Permission )
class PermissionAdmin (admin .ModelAdmin ):
    list_filter =('content_type',)
    list_display =('id','name','content_type','codename')
    list_per_page =20 
    search_fields =('name','codename')
@admin .register (LogEntry )
class LogEntryAdmin (admin .ModelAdmin ):
    list_display =('id','user','content_type','action_flag','action_time')
    list_filter =('user','content_type','action_flag','action_time')
    list_per_page =20 
