from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from recipes.models import Follow
from users.models import User


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email')


admin.site.register(User, UserAdmin)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')


admin.site.register(Follow, FollowAdmin)
