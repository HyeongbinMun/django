from django.contrib import admin
from .models import Game, Category

class GameAdmin(admin.ModelAdmin):
    serach_fields = ['subject']

# Register your models here.
admin.site.register(Game, GameAdmin)
admin.site.register(Category)