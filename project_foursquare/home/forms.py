from django import forms

from .models import Mall

class PostForm(forms.ModelForm):

    class Meta:
        model = Mall
        fields = ('image','nama_mall','lokasi_mall','deskripsi_mall','map_mall','fasilitas_1','fasilitas_2','fasilitas_3','fasilitas_4')