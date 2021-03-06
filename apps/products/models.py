from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    stock = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if self.stock > 0:
            self.is_active = True
        else:
            self.is_active = False

        super(Product, self).save(*args, **kwargs)
