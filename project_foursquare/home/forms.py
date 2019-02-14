from django import forms

from .models import Mall, Park

class PostForm1(forms.ModelForm):

    class Meta:
        model = Mall
        fields = ('image','nama_mall','lokasi_mall','deskripsi_mall','map_mall','fasilitas_1','fasilitas_2','fasilitas_3','fasilitas_4')

class PostForm2(forms.ModelForm):

   class Meta:
       model = Park
       fields = ('nama', 'lokasi','gambar','deskripsi','map_park','fasilitas_1','fasilitas_2','fasilitas_3','fasilitas_4')
