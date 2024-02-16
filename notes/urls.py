from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
# from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('notes/', NoteViewSet.as_view({'get': 'list'}), name='notes_list'),
    path('notes/<uuid:pk>/', NoteViewSet.as_view({'get': 'retrieve'}), name='notes_detail'),
]
