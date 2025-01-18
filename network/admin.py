from django.contrib import admin
from django.utils.html import format_html
from network.models import SalesNetwork, Product
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class SalesNetworkForm(ModelForm):
    """Форма для создания/редактирования SalesNetwork"""
    class Meta:
        model = SalesNetwork
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        network_type = cleaned_data.get("network_type")
        supplier = cleaned_data.get("supplier")
        # Валидация иерархии типа завода с поставщиком
        if network_type == "FA" and supplier.network_type in ["NW", "IE"]:
            raise ValidationError(f"У завода не может быть поставщик, кроме другого завода ")
        # Валидация иерархии типа розничной сети с поставщиком
        if network_type == "NW" and supplier.network_type in ["IE"]:
            raise ValidationError("У розничной сети не может быть поставщик индивидуальный предприниматель")

        return cleaned_data


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение модели Product в админке"""
    list_display = ('id', 'name', 'model', 'release_date',)


@admin.register(SalesNetwork)
class SalesNetworkAdmin(admin.ModelAdmin):
    """Отображение модели SalesNetwork в админке"""
    form = SalesNetworkForm
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
