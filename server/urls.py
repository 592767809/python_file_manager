
from django.contrib import admin
from django.urls import path, re_path
from server import views
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('file', views.file_manager),
    re_path('^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
