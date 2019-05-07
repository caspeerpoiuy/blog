from django.conf.urls import url

from applications.tools import views

urlpatterns = [
    url(r"^lagou/$", views.LagouSpiderApiView.as_view()),
]
