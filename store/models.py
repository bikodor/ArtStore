
import uuid
from django.db import models
from django.urls import reverse

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name="products")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")
    price = models.IntegerField()
    short_desc = models.CharField(max_length=100, blank=True, verbose_name="Краткое описание")
    description = models.TextField(max_length=255, blank=True, verbose_name="Полное описание товара", default='No description')
    rating = models.FloatField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    attrs = models.ManyToManyField('Attributes', blank=True, related_name='products')  # related_name="products"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'id': self.id})

    objects = models.Manager()

class Attributes(models.Model):
    attribute = models.TextField()

    def __str__(self):
        return self.attribute

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cats', kwargs={'cat_slug': self.slug})

