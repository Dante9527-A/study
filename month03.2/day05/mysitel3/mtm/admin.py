from django.contrib import admin
from .models import *

# Register your models here.
class AuthorManage(admin.ModelAdmin):
    list_display = ['id','name']

class BookManage(admin.ModelAdmin):
    list_display = ['id','title']



admin.site.register(Author,AuthorManage)
admin.site.register(Book,BookManage)