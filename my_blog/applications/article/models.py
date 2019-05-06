from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    parent_category = models.ForeignKey('self',blank=True, null=True, on_delete=models.CASCADE)
    create_time = models.DateField(default=timezone.now)
    update_time = models.DateField(default=timezone.now)

    class Meta:
        db_table = "BlogCategory"


class Tag(models.Model):
    name = models.CharField('标签名', max_length=30, unique=True)

    class Meta:
        db_table = "BlogTag"


class ArticleModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField(null=False)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cate = models.ForeignKey(Category,on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)

    class Meta:
        db_table = "BlogArticle"


