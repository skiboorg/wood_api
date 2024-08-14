from decimal import Decimal

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

def get_cart(request) -> Cart:
    session_id = request.query_params.get('session_id', None)
    print('session_id',session_id)
    cart, _ = Cart.objects.get_or_create(session_uuid=session_id)
    return cart

class CartView(APIView):
    def get(self, request):
        cart = get_cart(request)
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data, status=200)

    def delete(self, request):
        print(request.data)
        result = {}
        return Response(status=200)

    def patch(self, request):
        print(request.data)
        item = CartItem.objects.get(id=request.data['product_id'])
        amount = Decimal(request.data['amount'])
        if amount > 0:
            item.amount = amount
            item.save()
        else:
            item.delete()
        result = {}
        return Response(result,status=200)

    def post(self, request):
        print(request.data)
        cart = get_cart(request)
        cart_item,created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=request.data['product_id'],
            unit_id=request.data['unit_id']

        )
        if created:
            print('created')
            cart_item.amount = request.data['amount']
            cart_item.save()
        else:
            print('updated')
            cart_item.amount += Decimal(request.data['amount'])
            cart_item.save()

        result = {}
        return Response(result, status=200)


