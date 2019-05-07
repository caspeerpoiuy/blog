from rest_framework.generics import ListAPIView

from .serializers import CategorySerializer,ArticleSerializer
from .models import CategoryModel, ArticleModel


class CategoryApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()


class ArticleApiView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return ArticleModel.objects.filter(id=category_id)


