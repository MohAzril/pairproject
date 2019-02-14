from django.db import models
from django.utils import timezone

# Create your models here.
class Mall(models.Model):
    nama = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to = 'images')
    deskripsi = models.TextField(max_length=500)

    def __str__(self):
        return self.nama

class Park(models.Model):
    nama = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to = 'images')
    deskripsi = models.TextField(max_length=500)

    def __str__(self):
        return self.nama