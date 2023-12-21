from rest_framework import serializers
from .models import Notes, Tags
    
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
    
    def create(self, validated_data):
        return Tags.objects.create(**validated_data)
    
class NoteSerializer(serializers.ModelSerializer):
    tags = TagsSerializer()
    class Meta:
        model = Notes
        fields = '__all__'
    
    def create(self, validated_data):
        return Notes.objects.create(**validated_data)