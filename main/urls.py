from django.urls import path
from main.content.views import ContextAPIView

urlpatterns = [
    # content app urls...
    path('context/', ContextAPIView.as_view())
]
