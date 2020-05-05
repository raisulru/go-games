from django.contrib import admin
from .models import Category, Game


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ('name', )

admin.site.register(Category, CategoryAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'image', 'category']
    search_fields = ('name', )
    filter_fields = ('category', )

admin.site.register(Game, GameAdmin)