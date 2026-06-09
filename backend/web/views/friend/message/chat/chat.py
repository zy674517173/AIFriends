import json

from django.http import StreamingHttpResponse
from langchain_core.messages import HumanMessage, BaseMessageChunk
from rest_framework.renderers import BaseRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.friend import Friend, Message
from web.views.friend.message.chat.graph import ChatGraph


class MessageChatView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        friend_id = request.data['friend_id']
        message = request.data['message'].strip()
        if not message:
            return Response({
                'result': '消息不能为空'
            })
        friends = Friend.objects.filter(pk=friend_id,me__user=request.user)
        if not friends:
            return Response({
                'result': '好友不存在'
            })
        friend = friends.first()

        # 下面对接大模型

        app = ChatGraph.create_app()

        inputs = {
            'message': [HumanMessage(message=message)]
        }
        res = app.invoke(inputs)
        print(res['message'][-1].content)

        return Response({
            'result': 'success',
        })
