from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]      #  强制必须登录才能访问，要求登录，但没有登录会返回 401， 401 身份验证失败
    def post(self, request):
        response = Response({
            'result': 'success',
        })
        response.delete_cookie('refresh_token')
        return response
