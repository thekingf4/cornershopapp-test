from django.contrib import admin
from order_system.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Circle admin"""

    list_display = ('email', 'username')

