from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    phone_number = PhoneNumberField(primary_key=True, blank=False, unique=True, max_length=15)    
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_created=True, default=timezone.now)

    def __str__(self):
        return f'{self.phone_number}'


class Chat(models.Model):
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, max_length=12, related_name="user_from")
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE, max_length=12, related_name="user_to")
    message = models.CharField(blank=False, null=False, max_length=5000)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)

    def __str__(self):
        return f'{self.sent_by} {self.sent_to} {self.message} {self.created_at}'
