from django.urls import path
from . import views


urlpatterns = [
    path('follower/<int:pk>', views.FollowerView.as_view()),
    path('follower', views.ListFollowerView.as_view())
]
