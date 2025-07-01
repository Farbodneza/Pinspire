from django.contrib import admin
from accounts.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'pk')
    search_fields = ('username',)
