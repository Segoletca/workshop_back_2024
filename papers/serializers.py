from rest_framework import serializers

from .models import Papers


class PapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Papers
        fields = '__all__'


class CreatePaperSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Papers
        fields = '__all__'
