from django.contrib import admin
from .models import Game, Category, Game_images

class categoryInline(admin.TabularInline):
    model = Category

class imageInline(admin.TabularInline):
    model = Game_images

class GameAdmin(admin.ModelAdmin):
    serach_fields = ['subject']
    inlines = [imageInline, categoryInline, ]

# Register your models here.
admin.site.register(Game, GameAdmin)