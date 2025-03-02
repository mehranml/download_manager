# downloader/urls.py
from django.urls import path
from downloader.views import add_download, downloads_list

urlpatterns = [
    path("", downloads_list, name="downloads_list"),
    path("add/", add_download, name="add_download"),
]
