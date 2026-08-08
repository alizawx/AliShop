from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    class Meta:
        ordering = ['name']
        indexes = [
        models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:products_by_category', args=[self.slug])


    def __str__(self):
        return self.name

class ProductFeature (models.Model) :
    name = models.CharField(max_length=255, verbose_name='نام ويزكى')
    value = models.CharField(max_length=255, verbose_name='مقدار ويشكي')

    def __str__(self) :
        return self.name + ":" + self.value



class Products(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=255, verbose_name="product")
    slug = models.SlugField(max_length=255)
    description = models.TextField(max_length=255)
    inventory = models.PositiveIntegerField(default=0, verbose_name=' مويوشى')
    price = models.PositiveIntegerField(default=0, verbose_name=' قيمة')
    off = models.PositiveIntegerField(default=0, verbose_name="")
    new_price = models.PositiveIntegerField(default=0, verbose_name="")
    features = models.ManyToManyField(ProductFeature, related_name='f_products', verbose_name="")
    created = models.DateTimeField(auto_now_add=True, verbose_name="")
    updated = models.DateTimeField(auto_now=True, verbose_name='' )

    class Meta:
        ordering = ['-created']
    indexes = [
        models.Index(fields=['id', 'slug']),
        models.Index(fields=[' name' ]),
        models.Index(fields=['-created']),
    ]
    verbose_name = ' محصول'
    verbose_name_plural = ' محصولها'


    def get_absolute_url(self):
        return reverse('shop:products_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name




class Image(models. Model):
    product = models. ForeignKey(Products, on_delete=models.CASCADE, related_name="images", verbose_name="")
    image_file = models.ImageField(upload_to="post_images")
    title = models.CharField(max_length=250, verbose_name="title", null=True, blank=True)
    description = models.TextField(verbose_name="details", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models. Index(fields=['created' ])
        ]
        verbose_name = 'picture'
        verbose_name_plural ="pictures"
