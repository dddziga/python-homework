from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assetc/images/brand/')

    def __str__(self):
        return self.name

class Key(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='assetc/images/keys/')

    def __str__(self):
        return self.name

