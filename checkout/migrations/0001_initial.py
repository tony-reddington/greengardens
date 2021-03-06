# Generated by Django 3.2.8 on 2021-11-17 13:37

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=250)),
                ('telephone_number', models.CharField(max_length=20)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('city_or_town', models.CharField(max_length=50)),
                ('county_or_state', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode_or_zip', models.CharField(blank=True, max_length=15, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date_of_order', models.DateTimeField(auto_now_add=True)),
                ('total_order', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('line_item_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
