from rest_framework.routers import DefaultRouter
from dj_rest_auth.views import LoginView
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('', include(router.urls)),
]