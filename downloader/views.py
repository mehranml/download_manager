import re

from django.shortcuts import render, redirect

from downloader.models import Download
from downloader.tasks import download_file


def add_download(request):
    if request.method == "POST":
        url: str = request.POST.get("url", "").strip()
        links = re.findall(r'https?://\S+', url)

        if not links:
            return render(request, "downloader/add_download.html", {"error": "No valid URL found!"})
        for link in links:
            download = Download.objects.create(url=link)
            download_file.delay(download.id)

        return redirect("downloads_list")

    return render(request, "downloader/add_download.html")


def downloads_list(request):
    downloads = Download.objects.all().order_by("-created_at")
    return render(request, "downloader/downloads_list.html", {"downloads": downloads})
