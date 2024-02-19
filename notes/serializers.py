from rest_framework import serializers
from .models import Notes
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class NoteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer() 

    class Meta:
        model = Notes
        fields = '__all__'
