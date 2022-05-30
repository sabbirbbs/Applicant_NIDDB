from django.contrib import admin
from .model import *

class NID_Data(admin.ModelAdmin):
    search_fields = ['status','pk','added_by__username','nid','date']
    readonly_fields = ['pk']

admin.site.register(Applicant_Data,NID_Data)