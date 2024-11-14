from rest_framework import serializers

from django.contrib.auth.models import User

from papers.models import Author


class UserViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class WhoAmIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
