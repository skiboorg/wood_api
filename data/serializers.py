from rest_framework import serializers
from .models import *



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'

class CallbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackForm
        fields = '__all__'

        extra_kwargs = {
            'phone': {"error_messages": {"required": "Телефон обязательное поле"},'required': True},

        }