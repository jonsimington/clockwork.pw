from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, Application

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

class ApplicationInline(admin.StackedInline):
    model = Application
    exclude = ("submitted", "updated")
    can_delete= False
    verbose_name_plural = "application"
    
class FancyUserAdmin(UserAdmin):
    inlines = (UserProfileInline, ApplicationInline)

admin.site.unregister(User)
admin.site.register(User, FancyUserAdmin)
