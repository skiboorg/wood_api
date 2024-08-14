import json
from decimal import Decimal

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser

class GetBanners(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class GetFaqs(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class NewForm(generics.CreateAPIView):
    queryset = CallbackForm
    serializer_class = CallbackFormSerializer
    # parser_classes = MultiPartParser



