from django.urls import path
from . import views

urlpatterns = [
    path('', views.RespondCreateView.as_view())
]
