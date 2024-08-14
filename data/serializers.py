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
            "name": {"error_messages": {"required": "Имя обязательное поле"}, 'required': True},
            'email': {"error_messages": {"required": "Email обязательное поле"},'required': True},
            'phone': {"error_messages": {"required": "Телефон обязательное поле"},'required': True},
            'file': {'required': False},
        }