from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, CharField, Serializer, IntegerField, StringRelatedField
from authapp.models import User
from django.contrib.auth.hashers import make_password, check_password
# from email.message import EmailMessage
import smtplib
# from library.settingsfolder.base import EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_USE_SSL
# from .smtp_mail import send_verification_email_task
# from djoser import serializers



class UserModelBaseSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'#['username', 'first_name', 'last_name', 'email']

    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data['password'])
    #     return super().create(validated_data)
    def create(self, validated_data):
        #send_verification_email_task(validated_data['email'])
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_superuser=validated_data.get('is_superuser', False),
            is_staff=validated_data.get('is_staff', False),
            is_active = validated_data.get('is_active', False)
            )
        return user
    



class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']