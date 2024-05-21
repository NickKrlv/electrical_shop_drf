from django.contrib import admin
from users.models import User
from .models import NetworkNode, Product


class ProductInline(admin.TabularInline):
    model = Product


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0)


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier', 'debt_to_supplier')
    search_fields = ('name', 'city')
    list_filter = ('city',)
    inlines = [ProductInline]
    actions = [clear_debt]


admin.site.register(NetworkNode, NetworkNodeAdmin)
admin.site.register(Product)
admin.site.register(User)
