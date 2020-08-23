from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexCreateView.as_view(), name='index'),
    path('log', views.log, name='log'),
    path('terminal',views.terminal, name='terminal'),
    path("check_command", views.check_command, name="check_command")
]