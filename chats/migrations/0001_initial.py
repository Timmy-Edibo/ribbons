# Generated by Django 4.0.4 on 2022-11-16 08:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('date_joined', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=15, primary_key=True, region=None, serialize=False, unique=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('message', models.CharField(max_length=5000)),
                ('sent_by', models.ForeignKey(max_length=12, on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to='chats.user')),
                ('sent_to', models.ForeignKey(max_length=12, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to='chats.user')),
            ],
        ),
    ]