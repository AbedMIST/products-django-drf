from django.db import models
from store.models import Store

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)  # Make optional
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products',
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
