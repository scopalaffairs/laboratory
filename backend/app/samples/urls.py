from django.urls import include, path
from .viewsets import ReadingAPIView

urlpatterns = [
    path('reading', ReadingAPIView.as_view()),
    path('reading/<str:pk>', ReadingAPIView.as_view()),
]
