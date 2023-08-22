from django import forms
from . import models


class PelatihForm(forms.ModelForm):
    class Meta:
        model = models.Pelatih
        fields = [
            "nama",
            "alamat",
            "deskripsi",
            "telp",
            "email",
        ]



class KejuaraanPelatihForm(forms.ModelForm):
    class Meta:
        model = models.KejuaraanPelatih
        fields = [
            "tahun",
            "kejuaraan",
            "medali",
            "foto",
        ]


class SertifikatPelatihForm(forms.ModelForm):
    class Meta:
        model = models.SertifikatPelatih
        fields = [
            "nama",
            "foto",
        ]


class jenis_skillForm(forms.ModelForm):
    class Meta:
        model = models.jenis_skill
        fields = [
            "rating",
            "nama_skill",
            "skill"
        ]

class perkembanganForm(forms.ModelForm):
    class Meta:
        model = models.perkembangan
        fields = [
            "kejuaraan",
            "namaBidang",
            "tahun",
        ]

class pengalamanForm(forms.ModelForm):
    class Meta:
        model = models.pengalaman
        fields = [
            "nama_pengalaman",
            "periode",
            "keterangan",
            "foto",
            "tahun",
        ]
