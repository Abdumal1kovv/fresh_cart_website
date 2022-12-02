from django.db.models import Model, ForeignKey, CASCADE, CharField, SlugField, ImageField, SmallIntegerField, TextField, \
    DateTimeField
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

from orders.models import upload_directory_name


class Category(MPTTModel):
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True, )
    slug = SlugField(max_length=255, unique=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        i = Category.objects.filter(slug=self.slug).count()
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += f'{i}'

        super().save(force_insert, force_update, using, update_fields)


class ProductImages(Model):
    product = ForeignKey('orders.Product', CASCADE)
    image = ImageField(upload_to=upload_directory_name)

    def __str__(self):
        return f'{self.product.name} -> {self.image.name}'


class Cart(Model):
    product = ForeignKey('orders.Product', CASCADE)
    user = ForeignKey('users.User', CASCADE)
    quantity = SmallIntegerField(default=1)

    @property
    def total_price(self):
        return sum(self.user.cart_set.values_list('product__price', flat=True))


class Comment(Model):
    product = ForeignKey('orders.Product', CASCADE)
    headline = CharField(max_length=255)
    text = TextField()
    author = ForeignKey('users.User', CASCADE)
    rate = SmallIntegerField(default=0)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)


class CommentImage(Model):
    product = ForeignKey('orders.Comment', CASCADE)
    picture = ImageField(upload_to='comments/')
