# Generated by Django 3.2.7 on 2021-09-24 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('0', 'Awaiting Payment'), ('1', 'Shipped'), ('2', 'Completed'), ('3', 'Cancelled'), ('4', 'Refunded')], default=0, max_length=1)),
                ('notes', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItems',
                'db_table': 'order_item',
            },
        ),
    ]
