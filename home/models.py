from django.db import models
from django.utils.html import format_html


# Create your models here.
class DefaultAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DefaultAbstract):
    title = models.CharField(max_length=255, verbose_name="Kategoriya: ")
    image = models.ImageField(verbose_name="Foto", blank=True, null=True, upload_to='category/')

    def __str__(self):
        return self.title

    @property
    def get_image(self):
        if self.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;" />'.format(self.image.url))
        return "No Image"


    class Meta:
        verbose_name_plural = "Kategoriyalar"


class Product(DefaultAbstract):
    user = models.ForeignKey('user.User', verbose_name="Adminstrator", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    price = models.IntegerField(verbose_name="Narxi")
    description = models.CharField(max_length=255, verbose_name="Tavsif")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Kategoriya", related_name='category',
                                 blank=True, null=True)
    quantity = models.IntegerField(verbose_name="Soni", default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Mahsulotlar"


class Gallery(models.Model):
    product = models.ForeignKey(Product, verbose_name='Mahsulot', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="Rasm")

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name_plural = "Galereya"


class Rating(DefaultAbstract):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    product = models.ForeignKey(Product, verbose_name="Mahsulot", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey('user.User', verbose_name="Foydalanuvchi", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Baholar"