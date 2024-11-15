from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
class UserAdmin(BaseUserAdmin):
  list_display=["username","date_of_birth"]
admin.site.register( User, UserAdmin)
