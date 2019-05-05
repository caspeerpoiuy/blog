import logging
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CommonUser
from .serializers import UserRegisterSerializer

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
