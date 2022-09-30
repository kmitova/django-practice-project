from django.urls import path, include

from practice_django_project.account.views import login_user, register_user, details_user

urlpatterns = (
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        ]))
)
