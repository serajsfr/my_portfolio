from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit-projects/<int:project_id>/', views.edit_projects, name='edit_projects'),
]
