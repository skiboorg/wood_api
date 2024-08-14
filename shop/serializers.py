from rest_framework import exceptions, serializers, status, generics


from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = '__all__'


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    features = ProductFeatureSerializer(many=True,required=False,read_only=True)
    images = ProductImageSerializer(many=True,required=False,read_only=True)
    units = ProductUnitSerializer(many=True,required=False,read_only=True)
    cat_slug = serializers.SerializerMethodField()
    cat_name = serializers.SerializerMethodField()
    subcat_slug = serializers.SerializerMethodField()
    subcat_name = serializers.SerializerMethodField()
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

    class Meta:
        model = Product
        fields = [
            'article',
            'is_new',
            'is_in_stock',
            'image',
            'name',
            'slug',
            'cat_slug',
            'subcat_slug',
            'subcat_name',
            'subcat_text'
        ]
    def get_image(self,obj):
        main_image = obj.images.filter(is_main=True)
        if main_image.exists():
            return main_image.first().image.url
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




class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['image','name','slug']


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