from django.db.models import CharField
from django.db.models import TextField
from django.db import models as models


# Create your models here.

class Park(models.Model):
    nama = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to = 'images')
    deskripsi = models.TextField(max_length=500)

    def __str__(self):
        return self.nama

class Mall(models.Model):
    image = models.ImageField(upload_to = 'images')
    nama_mall = models.CharField(max_length=255)
    lokasi_mall = models.CharField(max_length=255)
    deskripsi_mall = models.TextField()

    def __str__(self):
        return self.nama_mall

