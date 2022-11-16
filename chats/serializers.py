from .models import User, Chat
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'is_superuser', 'date_joined']

class ChatSerializer(serializers.ModelSerializer):
    sent_to = PhoneNumberField()
    sent_by =  PhoneNumberField()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Chat
        fields = ['sent_to', 'sent_by', 'message', 'created_at']
        

    def save(self):
        user_from = User.objects.get(phone_number = self.validated_data['sent_by'])
        user_to = User.objects.get(phone_number = self.validated_data['sent_to'])

        chat = Chat(
                    sent_to = user_to,
                    sent_by = user_from,
                    message = self.validated_data['message'],
                )

        chat.save()
        print(self.validated_data)
        return chat

