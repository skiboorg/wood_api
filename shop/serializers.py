from rest_framework import exceptions, serializers, status, generics


from .models import *
from django.conf import settings
from collections import defaultdict

class MaterialPropSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialTag
        fields = '__all__'


class UnitPropSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitWidth
        fields = '__all__'


class MaterialShortSerializer(serializers.ModelSerializer):
    tags = MaterialPropSerializer(many=True, read_only=True)
    recommend = MaterialPropSerializer(many=True, read_only=True)
    class Meta:
        model = Material
        fields = ['name','slug','image','tags','recommend','short_description']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductUnitSerializer(serializers.ModelSerializer):
    thin = UnitPropSerializer(many=False, read_only=True)
    width = UnitPropSerializer(many=False, read_only=True)
    length = UnitPropSerializer(many=False, read_only=True)
    class Meta:
        model = ProductUnit
        fields = '__all__'




class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = '__all__'


class ProductFeatureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeatureDetail
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    features = ProductFeatureDetailSerializer(many=True,required=False,read_only=True)
    images = ProductImageSerializer(many=True,required=False,read_only=True)
    units = ProductUnitSerializer(many=True,required=False,read_only=True)

    cat_slug = serializers.SerializerMethodField()
    cat_name = serializers.SerializerMethodField()
    subcat_slug = serializers.SerializerMethodField()
    subcat_name = serializers.SerializerMethodField()
    material = MaterialShortSerializer(many=False, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
    def get_cat_slug(self,obj):
        return obj.subcategory.category.slug
    def get_cat_name(self,obj):
        return obj.subcategory.category.name
    def get_subcat_slug(self,obj):
        return obj.subcategory.slug

    def get_subcat_name(self,obj):
        return obj.subcategory.name



class ProductShortSerializer(serializers.ModelSerializer):
    cat_slug = serializers.SerializerMethodField()
    subcat_slug = serializers.SerializerMethodField()
    subcat_name = serializers.SerializerMethodField()
    subcat_text = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    features = ProductFeatureSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Product
        fields = [
            'article',
            'image',
            'name',
            'slug',
            'cat_slug',
            'subcat_slug',
            'subcat_name',
            'subcat_text',
            'display_price',
            'features'
        ]
    def get_image(self,obj):
        main_image = obj.images.filter(is_main=True)
        if main_image.exists():
            return f'{settings.IMG_URL}{main_image.first().image.url}'
        else:
            return None
    def get_cat_slug(self,obj):
        return obj.subcategory.category.slug
    def get_subcat_slug(self,obj):
        return obj.subcategory.slug
    def get_subcat_name(self,obj):
        return obj.subcategory.name
    def get_subcat_text(self,obj):
        return obj.subcategory.short_description


class SubCategorySerializer(serializers.ModelSerializer):
    #products = ProductSerializer(many=True, required=False, read_only=True)
    products = serializers.SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = '__all__'

    def get_products(self, obj):
        active_products = obj.products.filter(is_active=True)
        return ProductSerializer(active_products, many=True).data

class SubCategoryShortSerializer(serializers.ModelSerializer):
    #products = ProductShortSerializer(many=True, required=False, read_only=True)
    products = serializers.SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = '__all__'
    def get_products(self, obj):
        active_products = obj.products.filter(is_active=True)
        return ProductShortSerializer(active_products, many=True).data


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryShortSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryForShortCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name','slug']

class CategoryShortSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryForShortCategorySerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Category
        fields = ['image','name','slug','display_amount','sub_categories']


class ServicePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePrice
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    prices = ServicePriceSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Service
        fields = '__all__'


class ServiceShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'





class MaterialSerializer(serializers.ModelSerializer):
    material_products = serializers.SerializerMethodField()
    class Meta:
        model = Material
        fields = '__all__'

    def get_material_products(self, obj):
        active_products = obj.material_products.filter(is_active=True)
        return ProductShortSerializer(active_products, many=True).data