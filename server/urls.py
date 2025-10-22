
from server import views
from django.urls import path


urlpatterns = [
    path('file', views.file_manager),
]
