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
        queryset = Notes.objects.all().order_by('created_at')
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        tag_data = request.data.get('tags', {})
        
        try:
            tag_instance = Tags.objects.get(name=tag_data.get('name'), color=tag_data.get('color'))
        except Tags.DoesNotExist:
            tag_instance = Tags.objects.create(name=tag_data.get('name'), color=tag_data.get('color'))
        
        note_id = request.data.get('id')
        if note_id:
            try:
                note_instance = Notes.objects.get(id=note_id)
                note_instance.title = request.data.get('title', '')
                note_instance.description = request.data.get('description', '')
                note_instance.tags.set([tag_instance])
                note_instance.save()
            except Notes.DoesNotExist:
                return Response({'error': 'Note with specified id does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            note_instance = Notes.objects.create(
                title=request.data.get('title', ''),
                description=request.data.get('description', ''),
            )
            note_instance.tags.set([tag_instance])

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = NoteSerializer

    @csrf_exempt
    def list(self, request):
        queryset = Tags.objects.all()
        serializer = TagsSerializer(queryset, many=True)
        return Response(serializer.data)