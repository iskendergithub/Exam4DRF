from django.contrib import admin
from .models import ShopDetail


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date']


admin.site.register(ShopDetail, ShopAdmin)