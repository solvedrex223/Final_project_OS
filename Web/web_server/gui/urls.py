from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexCreateView.as_view(), name='index'),
    path('terminal',views.terminal, name='terminal'),
    path("check_command", views.check_command, name="check_command"),
    path("check_user", views.check_user, name="check_user"),
    path("new_user", views.new_user, name="new_user"),
]