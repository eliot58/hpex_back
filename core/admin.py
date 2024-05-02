from django.contrib import admin
from django.forms import Textarea
from django.http import HttpRequest
from .models import *

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, *args, **kwargs) -> bool:
        return False
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':30, 'cols': 140})},
    }
    list_display = ['id', 'text']

@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, *args, **kwargs) -> bool:
        return False
    list_display = ["id", 'text']


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'date_of_birth', 'phone', 'username', 'city', 'transport', 'code', 'created']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'phone',  'city',  'code', 'created'] 


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'created']

    @admin.display(description='Название файла')
    def file_name(self, obj):
        return obj.file.name.split("/")[1]

@admin.register(Ransom)
class RansomAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'created']

    @admin.display(description='Название файла')
    def file_name(self, obj):
        return obj.file.name.split("/")[1]