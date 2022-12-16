from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(VideoComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','user','parent_name','comment']

@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']