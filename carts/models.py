from django.db import models


class Cart(models.Model):
    class Meta:
        ordering = ["id"]

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="cart"
    )
