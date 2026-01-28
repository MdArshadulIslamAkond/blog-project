from django.contrib import admin
from .models import MenuList, UserPermission, Post
# Register your models here.

admin.site.register(MenuList)
admin.site.register(UserPermission)
admin.site.register(Post)