from django.urls import path
from .views import LessonView, lessons

app_name = 'conspect'


urlpatterns = [
    path('', LessonView.as_view(), name='lessons'),
    path('lessons/', lessons, name='lessons_tmp'),
]