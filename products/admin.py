from django.contrib import admin

from products.models import Product, ProductCategory, Basket

# admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    list_filter = ("category",)
    search_fields = ('name',)
    ordering = ('name', 'price')
    fields = ('name', ('price', 'quantity', 'category'), 'image', 'description', 'short_description')
    readonly_fields = ('short_description', 'description')


class BasketAdminInline(admin.TabularInline):
    model = Basket
    filter = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)