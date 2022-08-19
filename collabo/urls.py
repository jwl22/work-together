from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:project_id>/', views.detail)
]