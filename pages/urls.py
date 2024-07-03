from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit-projects/<int:project_id>/', views.edit_projects, name='edit_projects'),
    path('accounts/', include('django.contrib.auth.urls')),
]
