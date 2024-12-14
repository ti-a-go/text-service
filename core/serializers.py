from rest_framework import serializers

from core.models import TextModel


class CreateTextModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextModel
        fields = ["title", "author", "text"]

class CreatedTextModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextModel
        fields = ["id", "title", "author", "text"]

class ListTextsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextModel
        fields = ["id", "title", "author", "text"]
