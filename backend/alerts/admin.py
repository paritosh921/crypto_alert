from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'coin', 'target_price', 'status', 'created_at')
    search_fields = ('coin', 'user__username')
    list_filter = ('status',)