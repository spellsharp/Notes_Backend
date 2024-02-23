from rest_framework import viewsets, status
from .models import Notes
from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def list(self, request):
        global_search = request.query_params.get('global_search', None)
        local_search = request.query_params.get('local_search', None)
        queryset = Notes.objects.all()
        if global_search:
            queryset = queryset.filter(is_public=True, title__contains=global_search)
            # print(queryset.query)
        elif local_search:
            queryset = queryset.filter(author=request.user, title__contains=local_search)
        else:
            queryset = queryset.filter(author=request.user)
        
        serializer = NoteSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        note_instance = Notes.objects.create(
            title = request.data.get('title', ''),
            description = request.data.get('description', ''),
            is_public = request.data.get('is_public', False),
            author = request.user
        )

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        note_instance = self.get_object()
        note_instance.title = request.data.get('title', note_instance.title)
        note_instance.description = request.data.get('description', note_instance.description)
        note_instance.deadline = request.data.get('deadline', note_instance.deadline)
        note_instance.is_public = request.data.get('is_public', note_instance.is_public)
        note_instance.save()

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


