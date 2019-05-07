from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from applications.account.models import CommonUser


class LagouSpiderApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = CommonUser.objects.get(username=request.user.username)
        if not user.email:
            return Response({"msg": "please add your eamil and use this function"})
        