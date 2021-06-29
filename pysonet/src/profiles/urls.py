
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.UserNetPrivateView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('profile/<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'})),

]
