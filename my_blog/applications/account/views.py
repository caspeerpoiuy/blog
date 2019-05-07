import logging
import uuid
# from django.core.cache
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from .models import CommonUser, UserCode
from .serializers import UserRegisterSerializer, UserBaseInfoSerializer, EmailSerializer

# logger = logging.getLogger(__name__)


class UserRegisterCountApiView(APIView):

    def get(self, request, username):
        count = CommonUser.objects.filter(username=username).count()
        data = {
            "username": username,
            "count": count
        }
        return Response(data)


class UserRegisterApiView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.data.pop("password")
        return Response(serializer.data)


class UserBaseInfoApiView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserBaseInfoSerializer

    def get_object(self):
        return self.request.user


class UserCodeGenerateApiView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        code = uuid.uuid1()
        UserCode.objects.create(code=code)
        return Response({"code": code})


class EmailApiView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmailSerializer

    def get_object(self):
        return self.request.user


class AvatarUploadApiView(APIView):

    def post(self, request):
        a = request.data
        return Response(a)