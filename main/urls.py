from django.urls import path
from main.content.views import CategoryListAPIView, ContentDetail

urlpatterns = [
    # content app urls...
    path('categories/', CategoryListAPIView.as_view()),
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', ContentDetail.as_view()),
]
