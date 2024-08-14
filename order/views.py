from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class OrderView(APIView):
    def get(self, request):
        print(request.data)
        result = {}
        return Response(status=200)

    def delete(self, request):
        print(request.data)
        result = {}
        return Response(status=200)

    def patch(self, request):
        print(request.data)
        result = {}
        return Response(result,status=200)

    def post(self, request):
        print(request.data)
        result = {}
        return Response(result, status=200)


