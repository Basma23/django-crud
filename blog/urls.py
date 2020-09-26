from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostesView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('blog/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('blog/new', PostCreateView.as_view(), name = 'post_create'),
    path('blog/<int:pk>/update', PostUpdateView.as_view(), name = 'post_update'),
    path('blog/<int:pk>/delete', PostDeleteView.as_view(), name = 'post_delete'),
    path('postes', PostesView.as_view(), name = 'postes'),
]