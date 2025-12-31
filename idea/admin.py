from django.contrib import admin
from .models import *


@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','num_pages')
    fields = (
        'title',
        'author',
        'pdf_file',
    )