from django.contrib import admin
from .models import Notes
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'deadline', 'updated_at')
    list_display = ('title', 'description', 'deadline', 'created_at', 'updated_at')

admin.site.register(Notes, NotesAdmin)