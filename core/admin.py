from django.contrib import admin
from core.models import Pin

# Register your models here.
@admin.register(Pin)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk')
    search_fields = ('title', 'tags')