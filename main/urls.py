from django.urls import path
from main.content.views import ContentDetail
from main.views import CategoryListAPIView, HomeAPIView

urlpatterns = [
    # main app urls...
    path('', HomeAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),

    # content app urls...
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', ContentDetail.as_view()),
]
