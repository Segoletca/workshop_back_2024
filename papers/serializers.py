from rest_framework import serializers

from .models import Papers


class PapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Papers
        fields = ['title', 'author', 'content', 'time_create', 'category']
        display_field = 'category__name'


class CreatePaperSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Papers
        fields = ['title', 'author', 'content', 'time_create', 'category']
        display_field = 'category__name'
