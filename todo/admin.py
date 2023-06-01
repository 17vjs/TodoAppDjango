from django.contrib import admin


from .models import Task,Tag
class TaskAdmin(admin.ModelAdmin):
    fields=["title","description","due_date","status","tags"]
    list_display = ["title", "timestamp", "was_added_recently"]
    list_filter = ["timestamp"]
    search_fields = ["title"]

admin.site.register(Task,TaskAdmin)
admin.site.register(Tag)

