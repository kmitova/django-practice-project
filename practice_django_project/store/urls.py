from django.urls import path

from practice_django_project.store.views import store_main_page

urlpatterns = (
    path('', store_main_page, name='store main page'),
)