from django.contrib import admin
from .models import *


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Articles, ArticlesAdmin)