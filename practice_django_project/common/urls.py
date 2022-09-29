from django.urls import path

from practice_django_project.common.views import index

urlpatterns = (
    path('', index, name='index'),
)