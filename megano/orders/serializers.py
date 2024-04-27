from rest_framework import serializers
from .models import Order
from products.serializers import ProductSerializer


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'phone',
            'fullName',
            'email',
            'createdAt',
            'deliveryType',
            'paymentType',
            'totalCost',
            'status',
            'city',
            'address',
            'products',
        )
    products = ProductSerializer(
        many=True,
        required=True,
    )
    fullName = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    def get_fullName(self, instance):
        return instance.user.profile.fullName

    def get_email(self, instance):
        return instance.user.profile.email

    def get_phone(self, instance):
        return instance.user.profile.phone
