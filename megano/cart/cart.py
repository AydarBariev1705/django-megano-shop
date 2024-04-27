from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart(object):
    """
    Объект корзины
    """
    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, count=1,):
        """
        Добавить или изменеить количество товаров в корзине
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'count': count,
                                     'price': str(product.price)}
        else:
            self.cart[product_id]['count'] += count
        self.save()

    def save(self):
        """
        Сохранить корзину
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product,):
        """
        Удаление товара из корзины или  уменьшение его количества
        """
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['count'] > 1:
                self.cart[product_id]['count'] -= 1
            else:
                del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине.
        А так же получение продуктов из базы данных
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for prod in self.cart.values():
            prod['price'] = Decimal(prod['price'])
            prod['total_price'] = prod['price'] * prod['count']
            yield prod

    def __len__(self):
        """
        Подсчет всех товаров в корзине
        """
        return sum(prod['count'] for prod in self.cart.values())

    def clear(self):
        """
        Очистка корзины
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def total_summ(self):
        """
        Общая сумма товаров в заказе
        """
        return sum(
            [Decimal(
                prod['price'],
            ) * prod['count'] for prod in self.cart.values()],
        )
