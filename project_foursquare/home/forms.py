from django import forms
from .models import Park

class PostForm(forms.ModelForm):

   class Meta:
       model = Park
       fields = ('nama', 'lokasi','gambar','deskripsi','map_park','fasilitas_1','fasilitas_2','fasilitas_3','fasilitas_4')
