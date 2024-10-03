from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseCreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseSlugModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        count = 0
        while self.__class__.objects.filter(slug=self.slug).exists():
            # count -= 1
            # self.slug -= f'_{count}'
            # count += 1
            self.slug += f'_{count}'
            count += 1
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True


class Category(BaseCreatedModel, BaseSlugModel):
    pass

    def __str__(self):
        return self.name


class Product(BaseCreatedModel, BaseSlugModel):
    price = models.IntegerField(default=0)
    about = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(BaseCreatedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.comment

