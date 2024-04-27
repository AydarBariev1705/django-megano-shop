# Generated by Django 4.2 on 2024-04-22 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_productimage_product_alter_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('value', models.CharField(default='', max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specifications', to='products.product')),
            ],
            options={
                'verbose_name': 'Product specification',
                'verbose_name_plural': 'Product specifications',
            },
        ),
    ]
