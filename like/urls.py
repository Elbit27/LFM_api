from django.urls import path
from . import views

urlpatterns = [
    path('', views.LikeCreateView.as_view()),
    path('<int:pk>/', views.LikeDeleteView.as_view()),
]
