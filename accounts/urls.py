from django.urls import path, include
from .import views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('dashboard/<str:username>/', views.UserDashboard.as_view(), name='dashboard')


]