from django.contrib import admin

from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'rent_per_month','timestamp']
    prepopulated_fields = {'slug': ('title',)}