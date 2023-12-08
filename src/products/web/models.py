from django.db import models
from django.core.files.storage import default_storage


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=False)

    
    def delete(self, *args, **kwargs):
        if self.image:
            image_path = self.image.path
            default_storage.delete(image_path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name