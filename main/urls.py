from django.urls import path
from .views import ContextAPIView, TopicAPIView

urlpatterns = [
    path('', ContextAPIView.as_view()),
    path('<slug>/<topic_slug>/', TopicAPIView.as_view()),
]
