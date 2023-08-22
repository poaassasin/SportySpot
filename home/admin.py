from django.contrib import admin
from django import forms

from . import models


class PelatihAdminForm(forms.ModelForm):

    class Meta:
        model = models.Pelatih
        fields = "__all__"


class PelatihAdmin(admin.ModelAdmin):
    form = PelatihAdminForm
    list_display = [
        "last_updated",
        "nama",
        "alamat",
        "deskripsi",
        "created",
        "telp",
        "email",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class KejuaraanPelatihAdminForm(forms.ModelForm):

    class Meta:
        model = models.KejuaraanPelatih
        fields = "__all__"


class KejuaraanPelatihAdmin(admin.ModelAdmin):
    form = KejuaraanPelatihAdminForm
    list_display = [
        "tahun",
        "last_updated",
        "kejuaraan",
        "created",
        "medali",
        "foto",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class SertifikatPelatihAdminForm(forms.ModelForm):

    class Meta:
        model = models.SertifikatPelatih
        fields = "__all__"


class SertifikatPelatihAdmin(admin.ModelAdmin):
    form = SertifikatPelatihAdminForm
    list_display = [
        "created",
        "nama",
        "last_updated",
        "foto",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class jenis_skillAdminForm(forms.ModelForm):

    class Meta:
        model = models.jenis_skill
        fields = "__all__"


class jenis_skillAdmin(admin.ModelAdmin):
    form = jenis_skillAdminForm
    list_display = [
        "created",
        "rating",
        "last_updated",
        "nama_skill",
        "skill"
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class pengalamanAdminForm(forms.ModelForm):

    class Meta:
        model = models.pengalaman
        fields = "__all__"

class perkembanganAdminForm(forms.ModelForm):
    
    class Meta:
        model = models.perkembangan
        fields = "__all__"


class perkembanganAdmin(admin.ModelAdmin):
    form = perkembanganAdminForm
    list_display = [
        "kejuaraan",
        "last_updated",
        "namaBidang",
        "created",
        "tahun",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class pengalamanAdmin(admin.ModelAdmin):
    form = pengalamanAdminForm
    list_display = [
        "nama_pengalaman",
        "periode",
        "keterangan",
        "created",
        "foto",
        "last_updated",
        "tahun",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Pelatih, PelatihAdmin)
admin.site.register(models.KejuaraanPelatih, KejuaraanPelatihAdmin)
admin.site.register(models.SertifikatPelatih, SertifikatPelatihAdmin)
admin.site.register(models.jenis_skill, jenis_skillAdmin)
admin.site.register(models.pengalaman, pengalamanAdmin)
admin.site.register(models.perkembangan, perkembanganAdmin)
