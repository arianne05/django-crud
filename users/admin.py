#this file allow to modify the django dashboard contents
from django.contrib import admin
from .models import User, Comment
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

#changes the django dashboard header
admin.site.site_header = "User Admin"
admin.site.site_title = "User Admin Area"

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0 #how many preview comment to display

class UserAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'user_fname', 'user_lname', 'user_email', 'user_position'] #add user database in django dashboard
    search_fields = ['user_fname', 'user_lname', 'user_email', 'user_position'] #add search function in django dashboard
    inlines = [CommentInline] #connected to class CommentInLine to display comments under the user

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'user_id', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active=True)


#for every class created need to register here
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)