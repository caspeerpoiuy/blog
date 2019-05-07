from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^catgories/$", views.CategoryApiView.as_view()),
    url(r"^catgories/(?P<category_id>\d+)/text/$", views.ArticleApiView.as_view()),
]
