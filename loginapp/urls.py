from django.urls import path
from knox import views as knox_views
from . import views


urlpatterns = [
    path('login/', views.userLogin),
    path('register_user/', views.userRegister),
    path('logout/',knox_views.LogoutView.as_view())
]
