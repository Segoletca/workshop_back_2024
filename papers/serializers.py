from rest_framework import serializers

from django.contrib.auth.models import User


class UserViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']