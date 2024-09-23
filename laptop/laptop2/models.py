from django.db import models


class Laptop(models.Model):
    BRAND_CHOICES = (
        ('mac os ', 'mac OS'),
        ('dell', 'dell'),
        ('hp', 'hp'),
        ('lenovo', 'lenovo'),
        ('asus', 'asus'),
    )
    brand = models.CharField(max_length=32, choices=BRAND_CHOICES)
    model = models.CharField(max_length=32)
    processor = models.CharField(max_length=32)
    ram_size = models.PositiveIntegerField(default=0)
    storage_size = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return f'{self.brand} - {self.model}'


class LaptopPhoto(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE,related_name='photos')
    image = models.ImageField(upload_to='img/')

    # def __sr__(self):
    #     return f'Photo of {self.laptop}'
