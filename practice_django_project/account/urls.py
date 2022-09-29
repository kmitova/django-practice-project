from django.urls import path

from practice_django_project.account.views import login_user

urlpatterns = (
    path('login/', login_user, name='login user'),
)