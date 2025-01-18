from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from network.models import SalesNetwork, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'release_date',)


@admin.register(SalesNetwork)
class SalesNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'network_type', 'email', 'country', 'city', 'street', 'house_number', 'get_supplier_link',
        'get_products', 'debt', 'created_at')
    list_display_links = ['id', 'name']
    list_filter = ['city', 'network_type', ]
    search_fields = ['city']
    actions = ['set_clear_debt']
    filter_horizontal = ['products']

    @admin.action(description='Очищение задолженности перед поставщиком')
    def set_clear_debt(self, request, queryset):
        count_update = queryset.update(debt=0)
        self.message_user(request, f"Задолженность успешно очищена у выбранных {count_update} объектов.")

    def get_supplier_link(self, obj):
        """ Возвращает ссылку на поставщика """
        if obj.supplier:
            url = obj.supplier.get_supplier_url()
            return format_html('<a href="{}">{}</a>', url, obj.supplier)

    get_supplier_link.short_description = "Поставщик"

    @admin.display(description="Товары электроники")
    def get_products(self, obj):
        """ Возвращает сам себя, предназначен для отображения названия колонки"""
        return list(obj.products.all())
