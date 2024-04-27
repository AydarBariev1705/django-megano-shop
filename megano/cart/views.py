from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from cart.serializers import BasketSerializer
from products.models import Product


def products_in_basket(cart: Cart) -> Response:
    products_ids = [product_id for product_id in cart.cart.keys()]
    products = Product.objects.filter(
        pk__in=products_ids,
    )
    serializer = BasketSerializer(
        products,
        many=True,
        context=cart.cart,
    )
    return Response(serializer.data)


class BasketView(APIView):
    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(
            Product,
            id=self.request.data.get('id'),
        )
        count = self.request.data.get('count')
        cart.add(
            product=product,
            count=count,
        )

        return products_in_basket(cart)

    def delete(self, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(
            Product,
            id=self.request.data.get('id'),
        )
        cart.remove(product, )
        return products_in_basket(cart)

    def get(self, *args, **kwargs):
        cart = Cart(self.request)
        return products_in_basket(cart)
