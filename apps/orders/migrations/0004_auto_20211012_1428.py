# Generated by Django 3.2.7 on 2021-10-12 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_is_active'),
        ('orders', '0003_auto_20210927_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='products.product'),
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('product', 'order')},
        ),
    ]