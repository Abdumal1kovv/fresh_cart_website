from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from orders.models import Product, Category, ProductImages, Comment, CommentImage


# @admin.register(ProductImages)
class ProductImagesTabularInline(TabularInline):
    model = ProductImages
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    exclude = ('slug',)
    inlines = (ProductImagesTabularInline,)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    search_fields = ['name']
    list_display = ['slug', 'name', 'id']
    exclude = ('slug',)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(parent=None)


class CommentImageTabularInline(TabularInline):
    model = CommentImage
    extra = 1


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    exclude = ('updated_at',)
    inlines = [CommentImageTabularInline]
