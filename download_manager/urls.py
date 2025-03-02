# download_manager/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("downloads/", include("downloader.urls")),
]
