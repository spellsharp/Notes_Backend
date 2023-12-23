from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, TagsViewSet
# from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('logout/', LogoutView.as_view(), name='auth_logout'),
    # path('register/', RegisterView.as_view(), name='auth_register'),
    path('notes/', NoteViewSet.as_view({'get': 'list'}), name='notes_list'),
    path('notes/<uuid:pk>/', NoteViewSet.as_view({'get': 'retrieve'}), name='notes_detail'),
    path('tags/', TagsViewSet.as_view({'get': 'list'}), name='tags_list'),
]
