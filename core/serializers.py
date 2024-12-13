from rest_framework import serializers

from core.models import TextModel


class CreateTextModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextModel
        fields = ["title", "author", "text"]
