from rest_framework import viewsets, status
from .models import Notes, Tags
from .serializers import NoteSerializer, TagsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

    @csrf_exempt
    def list(self, request):
        queryset = Notes.objects.all()
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        tag_data = request.data.get('tags', {})
        
        tag_instance, _ = Tags.objects.get_or_create(name=tag_data.get('name'), defaults={'color': tag_data.get('color')})
        
        note_instance = Notes.objects.create(
            title=request.data.get('title', ''),
            description=request.data.get('description', ''),
            tags=tag_instance
        )

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        tag_data = request.data.get('tags', {})
        
        tag_name = tag_data.get('name')
        tag_instance, _ = Tags.objects.get_or_create(name=tag_name, defaults={'color': tag_data.get('color')})
        
        note_instance = self.get_object()
        note_instance.title = request.data.get('title', note_instance.title)
        note_instance.description = request.data.get('description', note_instance.description)
        note_instance.tags = tag_instance
        note_instance.save()

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


        
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

    @csrf_exempt
    def list(self, request):
        queryset = Tags.objects.all()
        serializer = TagsSerializer(queryset, many=True)
        return Response(serializer.data)
