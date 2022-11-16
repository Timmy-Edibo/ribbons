from django.shortcuts import render
from django.http import HttpResponse
from .models import Chat, User
from django.http import Http404

from .serializers import UserSerializer, ChatSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q

class UserList(APIView):

    def get(self, request, format=None):
        query = User.objects.all()
        serializer = UserSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, phone_no):
            try:
                    return User.objects.get(phone_number=phone_no)
            except User.DoesNotExist as e:
                    raise Http404 from e

    def get(self, request, phone_no, format=None):
        users = self.get_object(phone_no)
        serializer = UserSerializer(users)
        return Response(serializer.data)


    def put(self, request, phone_no, format=None):
        user = self.get_object(phone_no)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, phone_no, format=None):
        user = self.get_object(phone_no)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChatList(APIView):

    def get(self, request, format=None):
        query = Chat.objects.all()
        serializer = ChatSerializer(query, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        x = User.objects.get(phone_number=request.data['sent_to'])
        y = User.objects.get(phone_number=request.data['sent_by'])
        lst = [x, y]

        notifier = [f"Admin {person}" if person.phone_number == "+2347067272110" else f"User {person}" for person in lst]
        messenger = f"{request.data['message']} {notifier}"
        request.data['message'] = messenger

        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            chat = serializer.save()
            data = {}
            data['sent_to'] = chat.sent_to
            data['sent_by'] = chat.sent_by
            data['message'] = f"{chat.message} {notifier}"
            x = f"{chat.message} {notifier}"
            print(messenger)

            # print(data['message'] == f"{chat.message} {notifier}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatDetail(APIView):

    def get(self, request, phone_no, format=None):
        users = Chat.objects.filter(
            Q(sent_to__phone_number__contains=phone_no) |
            Q(sent_by__phone_number__contains=phone_no) & Q(sent_to__phone_number__contains="+2347067272110")).all()
     
        serializer = ChatSerializer(users, many=True)
        return Response(serializer.data)


{"sent_to": "+2349022334455",
"sent_by": "+2347067272110",
"message": "do you need an ambulance and water"
}