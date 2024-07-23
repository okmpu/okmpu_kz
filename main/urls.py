from django.urls import path
from main.content.views import CategoryListAPIView, ContentDetail
from main.views import HomeAPIView

urlpatterns = [
    # main app urls...
    path('', HomeAPIView.as_view()),

    # content app urls...
    path('content/categories/', CategoryListAPIView.as_view()),
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', ContentDetail.as_view()),
]
