from django.contrib import admin
from .models import Notes
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'author', 'updated_at', 'deadline', 'is_public')    
    list_display = ('title', 'description', 'author', 'created_at', 'updated_at', 'deadline', 'is_public')

admin.site.register(Notes, NotesAdmin)