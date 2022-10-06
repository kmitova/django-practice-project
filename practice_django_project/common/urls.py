from django.urls import path

from practice_django_project.common.views import index, about, team, t_and_c, delivery, faq

urlpatterns = (
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('t-and-c/', t_and_c, name='t-and-c'),
    path('delivery/', delivery, name='delivery'),
    path('faq/', faq, name='faq'),
)