from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from cart.cart import Cart
from products.models import Product
from .serializers import OrdersSerializer
from .models import Order, CountProducts


class OrdersList(APIView):
    def get(self, request: Request) -> Response:
        orders = Order.objects.filter(user_id=request.user.pk)
        serialized = OrdersSerializer(orders, many=True)
        return Response(serialized.data)

    def post(self, request: Request, *args, **kwargs) -> Response:
        data = request.data
        products_in_order = [
            (obj['id'], obj['count'], obj['price']) for obj in data
        ]
        products_ids = [product_id[0] for product_id in products_in_order]
        products = Product.objects.filter(id__in=products_ids)
        order = Order.objects.create(
            user=request.user,
            totalCost=Cart(request).total_summ(),
        )
        order.products.set(products)
        order.save()

        return Response({
            'orderId': order.pk
        })


class OrderDetails(APIView):
    def get(self, request: Request, pk):
        data = Order.objects.get(pk=pk)
        serialized = OrdersSerializer(data)
        cart = Cart(request).cart
        data = serialized.data
        products_in_order = data['products']
        for prod in products_in_order:
            prod['count'] = cart[str(prod['id'])]['count']

        return Response(data)

    def post(self, request: Request, pk) -> Response:
        order = Order.objects.get(pk=pk)
        data = request.data
        order.fullName = data['fullName']
        order.phone = data['phone']
        order.email = data['email']
        order.deliveryType = data['deliveryType']
        order.city = data['city']
        order.address = data['address']
        order.paymentType = data['paymentType']
        order.status = 'awaiting'
        print('deliveryType', data['deliveryType'])

        for product in data['products']:
            CountProducts.objects.get_or_create(
                order_id=order.pk,
                product_id=product['id'],
                count=product['count'],
            )
        order.save()
        if data['deliveryType'] == 'express':

            order.totalCost += 500
        else:
            if order.totalCost < 2000:
                order.totalCost += 200
        order.save()

        return Response(data, status=status.HTTP_201_CREATED)


class Payment(APIView):
    def post(self, request: Request, pk) -> Response:
        order = Order.objects.get(pk=pk)
        order.status = 'accepted'
        order.save()
        Cart(request).clear()
        return Response(request.data, status=status.HTTP_200_OK)
