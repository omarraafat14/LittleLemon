from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'price', 'inventory')
    
admin.site.register(Booking)