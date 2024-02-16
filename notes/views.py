from rest_framework import viewsets, status
from .models import Notes
from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

    @csrf_exempt
    def list(self, request):
        # TODO: When the author is implemented, this will be used to filter the notes by author.
        # author = request.query_params.get('author', None)
        # queryset = Notes.objects.filter(author=author)

        # Comment this line after uncommenting the above line.
        queryset = Notes.objects.all()
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        note_instance = Notes.objects.create(
            title=request.data.get('title', ''),
            description=request.data.get('description', ''),
        )

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        note_instance = self.get_object()
        note_instance.title = request.data.get('title', note_instance.title)
        note_instance.description = request.data.get('description', note_instance.description)
        note_instance.deadline = request.data.get('deadline', note_instance.deadline)
        note_instance.save()

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)