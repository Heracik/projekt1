from django.urls import path
from . import views

app_name = 'agents'

urlpatterns = [
    path('', views.agent_list, name='agent_list'),
    path('<int:pk>/', views.agent_detail, name='agent_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), # Detail agenta podľa ID
]