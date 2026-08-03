from django.db import models

# Create your models here.

class Category(models. Model):
    name = models.CharField(max_length=255)
    slug = models. SlugField(max_length=255, unique=True)
    class Meta:
        ordering = ['name']
        indexes = [
        models. Index(fields=[' name' ])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
class ProductFeature (models.Model) :
    name = models. CharField(max_Length=255, verbose_name='نام ويزكى')
    value = models. CharField(max_Length=255, verbose_name='مقدار ويشكي')

    def __str__(self) :
        return self.name + ":" + self.value



class Products(models.Model):
    category = models.ForeignKey(Category, related_name=' products', on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=255, verbose_name="product")
    slug = models.SlugField(max_Length=255)
    description = models.TextField(max_length=255)
    inventory = models.PositiveIntegerField(default=0, verbose_name=' مويوشى')
    price = models.PositiveIntegerField(default=0, verbose_name=' قيمة')
    off = models.PositiveIntegerField(default=0, verbose_name="")
    new_price = models.PositiveIntegerField(default=0, verbose_name="")
    features = models.ManyToManyField(ProductFeature, related_name='f_products', verbose_name="")
    created = models.DateTimeField(autonow_add=True, verbose_name="")
    updated = models.DateTimeField(auto_now=True, verbose_name='' )


class Image(models. Model):
    product = models. ForeignKey(Products, on_delete=models.CASCADE, related_name="images", verbose_name="")
    image_file = models. ImageField(upload_to="post_images")
    title = models.CharField(max_Length=250, verbose_name=" alein", null=True, blank=True)
    description = models.TextField(verbose_name="amae", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
        indexes = [
            models. Index(fields=[' created' ])
        ]
        verbose_name = 'picture'
        verbose_name_plural ="pictures"
