# Generated by Django 4.2.10 on 2024-08-27 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import foodapp.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('catagory_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('catagory_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_staff',
            fields=[
                ('staff_id', models.CharField(default=foodapp.models.delivery_staff_unique_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.CharField(default=foodapp.models.generate_unique_code, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('item_name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to=foodapp.models.user_directory_path)),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('availability', models.BooleanField()),
                ('catagory_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigIntegerField(default=foodapp.models.generate_unique_code_order, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_address', models.CharField(max_length=200)),
                ('total_ammount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('order_status', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField(max_length=1000)),
                ('review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_method', models.CharField(max_length=100)),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Order_items',
            fields=[
                ('order_item_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('menu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.menu')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('delivery_status', models.CharField(max_length=100)),
                ('delivery_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.order')),
                ('staff_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.delivery_staff')),
            ],
        ),
    ]
