from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pk', 'color', 'rubric', 'photo', 'quantity']
    list_display_links = ['title', 'pk', 'color']
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class RubricAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Rubric, RubricAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Gender)