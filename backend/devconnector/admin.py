from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django.contrib.auth.models import Group


class UserModelAdmin(BaseUserAdmin):
    search_fields = ("email", "name")

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.search_fields = ['email']
        self.fieldsets = list(self.fieldsets)
        self.fieldsets[2] = (None, {'fields': ('is_superuser', )})
        self.filter_horizontal = ()
        self.list_display = ('id', 'email', 'name', 'is_superuser')


admin.site.unregister(Group)
admin.site.register(User, UserModelAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ("company",)
    list_display = ("id", "company", "website", "status")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("id", "title", "from_date", "to_date", "current")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "school", "degree", "from_date", "to_date")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("text", "name")
    list_display = ("id", "text", "name", "date")
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("text", )
    list_display = ("id", "text", "date")
    
