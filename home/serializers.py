from rest_framework import serializers

from . import models


class PelatihSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pelatih
        fields = [
            "last_updated",
            "nama",
            "alamat",
            "deskripsi",
            "created",
            "telp",
            "email",
        ]

class KejuaraanPelatihSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KejuaraanPelatih
        fields = [
            "tahun",
            "last_updated",
            "kejuaraan",
            "created",
            "medali",
            "foto",
        ]

class SertifikatPelatihSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SertifikatPelatih
        fields = [
            "created",
            "nama",
            "last_updated",
            "foto",
        ]

class perkembanganSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.perkembangan
        fields = [
            "kejuaraan",
            "last_updated",
            "namaBidang",
            "created",
            "tahun",
        ]

class jenis_skillSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.jenis_skill
        fields = [
            "created",
            "rating",
            "last_updated",
            "nama_skill",
            "skill"
        ]

class pengalamanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pengalaman
        fields = [
            "nama_pengalaman",
            "periode",
            "keterangan",
            "created",
            "foto",
            "last_updated",
            "tahun",
        ]
