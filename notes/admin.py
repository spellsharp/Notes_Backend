from django.contrib import admin
from .models import Notes, Tags
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'tags', 'created_at', 'updated_at')
    list_display = ('title', 'description', 'created_at', 'updated_at')

class TagsAdmin(admin.ModelAdmin):
    fields = ('name', 'color')
    list_display = ('name', 'color')

admin.site.register(Notes, NotesAdmin)
admin.site.register(Tags, TagsAdmin)