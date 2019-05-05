from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

urlpatterns = [
    url(r"^username/(?P<username>\w{6,20})/count/$", views.UserRegisterCountApiView.as_view()),
    url(r"^register/$", views.UserRegisterApiView.as_view()),
    url(r"^login/$", obtain_jwt_token),
    url(r"^refresh/$", refresh_jwt_token),
    url(r"^baseinfo/", views.UserBaseInfoApiView.as_view()),
    url(r"^code/", views.UserCodeGenerateApiView.as_view())
]
