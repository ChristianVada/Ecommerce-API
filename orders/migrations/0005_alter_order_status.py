# Generated by Django 4.0.7 on 2023-07-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('placed', 'Placed'), ('progress', 'Progress'), ('delivered', 'Delivered')], max_length=120),
        ),
    ]
