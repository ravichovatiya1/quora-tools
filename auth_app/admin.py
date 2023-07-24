from django.contrib import admin
from auth_app import models
# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name','is_staff',
                    'is_active','created_at')
