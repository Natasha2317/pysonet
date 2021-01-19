
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>/', views.UserNetView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'})),

]