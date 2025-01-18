from django.contrib import admin
from django.utils.html import format_html
from network.models import SalesNetwork, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'release_date',)


@admin.register(SalesNetwork)
class SalesNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'network_type', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'products',
        'created_at')
    list_display_links = ['id']
    list_filter = ['city']
    search_fields = ['city']
    actions = ['set_clear_debt']

    @admin.action(description='Очищение задолженности перед поставщиком')
    def set_clear_debt(self, request, queryset):
        count_update = queryset.update(debt=0)
        self.message_user(request, f"Задолженность успешно очищена у выбранных {count_update} объектов.")
