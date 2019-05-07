from rest_framework import serializers

from .models import CategoryModel, ArticleModel


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleModel
        fields = ["title", "views", "author", "cate", "update_time"]


