from rest_framework import serializers

from .models import Papers


class PapersSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Papers
        fields = '__all__'
