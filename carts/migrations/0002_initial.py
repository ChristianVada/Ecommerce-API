<<<<<<<< HEAD:carts/migrations/0002_initial.py
# Generated by Django 4.0.7 on 2023-07-06 20:10
========
# Generated by Django 4.0.7 on 2023-07-06 17:08
>>>>>>>> 0a977f0d4da1c1afec677e702d050aadbe132f14:addresses/migrations/0002_initial.py

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
<<<<<<<< HEAD:carts/migrations/0002_initial.py
        ('carts', '0001_initial'),
========
        ('addresses', '0001_initial'),
>>>>>>>> 0a977f0d4da1c1afec677e702d050aadbe132f14:addresses/migrations/0002_initial.py
    ]

    operations = [
        migrations.AddField(
<<<<<<<< HEAD:carts/migrations/0002_initial.py
            model_name='cart',
========
            model_name='address',
>>>>>>>> 0a977f0d4da1c1afec677e702d050aadbe132f14:addresses/migrations/0002_initial.py
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL),
        ),
    ]
