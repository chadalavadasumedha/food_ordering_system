# Generated by Django 3.1.3 on 2021-05-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_remove_order_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_type',
            field=models.CharField(blank=True, choices=[('HOME DELIVERY', 'HOME DELIVERY'), ('DINE IN', 'DINE IN')], default='HOME DELIVERY', max_length=100, null=True),
        ),
    ]
