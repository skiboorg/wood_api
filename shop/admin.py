from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.safestring import mark_safe
from .models import *
class ProductUnitInline(NestedStackedInline):
    model = ProductUnit
    extra = 0

class ProductFeatureInline(NestedStackedInline):
    model = ProductFeature
    extra = 0

class ProductFeatureDetailInline(NestedStackedInline):
    model = ProductFeatureDetail
    extra = 0



class ProductImageInline(NestedStackedInline):
    model = ProductImage
    extra = 0

class ProductAdmin(NestedModelAdmin):
    list_display = ('image_preview','article','name','subcategory','is_active',)
    model = Product
    inlines = [ProductUnitInline,ProductFeatureInline,ProductFeatureDetailInline,ProductImageInline]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        main_image = obj.images.filter(is_main=True)
        if main_image.exists():
            return mark_safe(
                '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(main_image.first().image.url))
        else:
            return 'Нет изображения'

    image_preview.short_description = 'Основное изображение'


class SubCategoryAdmin(NestedModelAdmin):
    list_display = ('name', 'category',)
    model = SubCategory

class ServicePriceInline(NestedStackedInline):
    model = ServicePrice
    extra = 0

class ServiceAdmin(NestedModelAdmin):
    list_display = ('name',)
    model = Service


admin.site.register(Category)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Material)
admin.site.register(MaterialTag)
admin.site.register(MaterialRecommend)
admin.site.register(UnitWidth)
admin.site.register(UnitLen)
admin.site.register(UnitThin)
