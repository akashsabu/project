from django.db import models
from django.core.files.storage import default_storage
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=False)

    
    def delete(self, *args, **kwargs):
        if self.image:
            image_path = self.image.path
            default_storage.delete(image_path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name