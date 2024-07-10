from django.urls import path
from .views import ContextAPIView, TopicAPIView, ContentAPIView

urlpatterns = [
    path('', ContextAPIView.as_view()),
    path('<slug>/<topic_slug>/', TopicAPIView.as_view()),
    path('<slug>/<topic_slug>/<chapter_slug>/<content_slug>/', ContentAPIView.as_view()),
]
