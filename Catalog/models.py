from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='category_name')
    description = models.TextField(verbose_name='category_description', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    description = models.TextField(verbose_name='description', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='image', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=50, verbose_name='category_name')
    price = models.IntegerField(verbose_name='price')
    create_date = models.DateField(verbose_name='create_date')
    change_date = models.DateField(verbose_name='last_change_date')

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
