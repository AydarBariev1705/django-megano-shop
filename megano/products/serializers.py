import datetime
from rest_framework import serializers
from .models import (Product,
                     Tag,
                     Review,
                     Sale,
                     Category,
                     ProductSpecification,
                     CategoryImage)


class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = (
            'id',
            'name',
            'value',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )


class ReviewSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = (
            'author',
            'email',
            'text',
            'rate',
            'date',
            'product',
        )

    def get_date(self, instance):
        date = instance.date + datetime.timedelta(hours=3)
        return datetime.datetime.strftime(
            date,
            format='%d.%m.%Y %H:%M',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'price',
            'count',
            'date',
            'title',
            'description',
            'fullDescription',
            'freeDelivery',
            'specifications',
            'tags',
            'images',
            'reviews'
        )

    images = serializers.SerializerMethodField()
    specifications = ProductSpecificationSerializer(
        many=True,
        required=False,
    )
    reviews = ReviewSerializer(
        many=True,
        required=False
    )
    tags = TagSerializer(
        many=True,
        required=False
    )
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        sale_price = instance.sales.first()
        if sale_price:
            instance.price = sale_price.salePrice

        return instance.price

    def get_images(self, instance):
        images = []
        for image in instance.images.all():
            images.append(
                {'src': f'/media/{image.__str__()}',
                 'alt': image.name},
            )
        return images


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = (
            'id',
            'src',
            'alt',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
            'parent',
        )

    image = CategoryImageSerializer(many=False)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
            'subcategories',
        )

    image = CategoryImageSerializer(
        many=False,
        required=False,
    )

    # image = serializers.SerializerMethodField()
    #
    # def get_image(self, instance):
    #     return {'src': f'/media/{instance.image.name}',
    #             'alt': f'{instance.image.name}'}

    subcategories = SubCategorySerializer(
        many=True,
        required=False,
    )


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = (
            'id',
            'salePrice',
            'dateFrom',
            'dateTo',
            'price',
            'title',
            'images',
        )

    images = serializers.SerializerMethodField()
    title = serializers.StringRelatedField()
    price = serializers.StringRelatedField()
    dateFrom = serializers.DateField(format='%d-%m')
    dateTo = serializers.DateField(format='%d-%m')

    def get_images(self, instance):
        images = []
        for image in instance.product.images.all():
            images.append(
                {'src': f'/media/{image.__str__()}',
                 'alt': image.name},
            )
        return images
