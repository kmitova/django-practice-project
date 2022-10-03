from django.urls import path, include

from practice_django_project.store.views import store_main_page, details_book

urlpatterns = (
    path('', store_main_page, name='store main page'),
    path('book/<int:pk>/', include([
        path('', details_book, name='details book'),
        ]))
)

