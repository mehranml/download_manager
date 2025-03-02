import os
import requests
from celery import shared_task
from django.conf import settings
from downloader.models import Download

DOWNLOAD_DIR = os.path.join(settings.BASE_DIR, "downloads")
# DOWNLOAD_DIR = '/media/admin/Seagate/mehran-media/downloads'

os.makedirs(DOWNLOAD_DIR, exist_ok=True)


@shared_task
def download_file(download_id):
    download = Download.objects.get(id=download_id)
    download.status = "downloading"
    download.save()

    try:
        response = requests.get(download.url, stream=True)
        filename = os.path.join(DOWNLOAD_DIR, download.url.split("/")[-1])

        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        download.file_path = filename
        download.status = "completed"
    except Exception as e:
        download.status = "failed"
    finally:
        download.save()
