from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_streams, name='streams'),
  path('<stream_name>/', views.get_stream_detail, name='stream_detail'),
]