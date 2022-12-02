from ckeditor.fields import RichTextField
from django.db.models import Model, ForeignKey, CASCADE, CharField, SlugField, DateTimeField, DecimalField, \
    SmallIntegerField, JSONField, TextField
from django.utils.text import slugify


def upload_directory_name(instance, filename):
    return f'products/{instance.product.id}/{filename}'


class Product(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, blank=True)
    price = DecimalField(decimal_places=2, max_digits=9)
    category = ForeignKey('orders.Category', CASCADE)
    promo_code = CharField(max_length=55)
    detail = RichTextField()
    quantity = SmallIntegerField(default=1)
    discount = SmallIntegerField(default=0)
    information = JSONField(default=dict)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    def stock(self):
        return 'In Stock' if self.quantity > 0 else 'Out of Stock'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        i = Product.objects.filter(slug=self.slug).count()
        while Product.objects.filter(slug=self.slug).exists():
            self.slug += f'{i}'

        super().save(force_insert, force_update, using, update_fields)
