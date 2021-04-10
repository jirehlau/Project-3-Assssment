from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
path('create/', views.create),
path('<int:w_id>/delete/', views.delete),
]