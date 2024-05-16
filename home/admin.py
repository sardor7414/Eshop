from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.image.url)
        return "No Image"

    get_image.short_description = 'Image'


class GalleryInline(admin.TabularInline):
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'price', 'category', 'quantity')
    list_display_links = ('name', )
    list_filter = ('user', 'name', 'price', 'category')
    inlines = (GalleryInline, )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('product', 'photo')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'user')
