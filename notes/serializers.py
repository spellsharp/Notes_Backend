from rest_framework import serializers
from .models import Notes, Tags

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(required=False)

    class Meta:
        model = Notes
        fields = '__all__'
