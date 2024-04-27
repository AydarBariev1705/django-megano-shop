# Generated by Django 4.2 on 2024-04-23 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_category_image_categoryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryimage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='products.category', verbose_name='category'),
        ),
    ]