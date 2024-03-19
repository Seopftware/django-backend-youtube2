from django.urls import path
from .views import (
    VideoList    
)

# api/v1/video
urlpatterns = [
    path('', VideoList.as_view(), name='video-list')
]