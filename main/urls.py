from django.urls import path
from .views import ContextAPIView, MainAPIView, TopicAPIView, ContentAPIView

urlpatterns = [
    path('', MainAPIView.as_view()),
    path('context/', ContextAPIView.as_view()),
    path('<slug>/<topic_slug>/', TopicAPIView.as_view()),
    path('<slug>/<topic_slug>/<chapter_slug>/<content_slug>/', ContentAPIView.as_view()),
]
