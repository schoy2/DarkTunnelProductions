from django.contrib import admin

# Register your models here.
from .models import MenuModel
'''
class MenuAdmin(admin.ModelAdmin):
    class Meta:
        model = MenuModel
'''
admin.site.register(MenuModel)#(MenuModel,MenuAdmin)
