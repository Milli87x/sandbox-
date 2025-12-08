from django.contrib import admin
from .models import profile


@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)
    # no list_filter on 'email' because profile model currently doesn't have that field
