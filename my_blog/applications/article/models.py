from django.db import models
from django.conf import settings
from django.utils import timezone


class CategoryModel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    create_time = models.DateField(default=timezone.now)
    update_time = models.DateField(default=timezone.now)

    class Meta:
        db_table = "BlogCategory"


class TagModel(models.Model):
    name = models.CharField('标签名', max_length=30, unique=True)
    create_time = models.DateField(default=timezone.now)
    update_time = models.DateField(default=timezone.now)

    class Meta:
        db_table = "BlogTag"


class ArticleModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField(null=False)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cate = models.ForeignKey(CategoryModel,on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField(TagModel, verbose_name='标签集合', blank=True)
    create_time = models.DateField(default=timezone.now)
    update_time = models.DateField(default=timezone.now)

    class Meta:
        db_table = "BlogArticle"


