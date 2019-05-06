from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('hw/',views.HwListAPIView.as_view()),
    path('hw/<int:pk>',views.HwDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)