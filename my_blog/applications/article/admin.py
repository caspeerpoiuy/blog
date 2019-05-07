from django.contrib import admin

from .models import CategoryModel,ArticleModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "body", "cate"]


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ArticleModel, ArticleAdmin)