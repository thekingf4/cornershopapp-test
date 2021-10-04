from django.contrib import admin
from order_system.menu.models import Menu, Ingredients, DetailMenu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Circle admin"""

    list_display = ('name', 'description')


@admin.register(Ingredients)
class IngredientAdmin(admin.ModelAdmin):
    """Circle admin"""

    list_display = ('pk', 'name', 'description', 'is_active')


@admin.register(DetailMenu)
class DetailMenuAdmin(admin.ModelAdmin):
    """Circle admin"""

    list_display = ('ingredient', 'menu')
