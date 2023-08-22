from django.db import models
from django.urls import reverse

SKILL_CHOICES = (
    ("1", "Berenang"),
    ("2", "Senam"),
    ("3", "Atletik"),
    ("4", "Fitness"),
    ("5", "Game Team"),
)

MEDALI_CHOICES = (
    ("Emas", "Emas"),
    ("Perak", "Perak"),
    ("Perunggu", "Perunggu"),
)
BIDANG_CHOICES = (
    ("Sepak Bola Indonesia", "Sepak Bola Indonesia"),
    ("Basket Indonesia", "Basket Indonesia"),
    ("Renang Indonesia", "Renang Indonesia"),
    ("Badminton Indonesia", "Badminton Indonesia"),
    ("Voli Indonesia", "Voli Indonesia"),
)

class KejuaraanPelatih(models.Model):

    # Relationships
    pelatih = models.ForeignKey("home.Pelatih", on_delete=models.CASCADE)

    # Fields
    medali = models.CharField(max_length=10, choices = MEDALI_CHOICES, default='Emas')
    tahun = models.CharField(max_length=4)
    kejuaraan = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    foto = models.ImageField(upload_to="upload/images/")

    class Meta:
        verbose_name_plural = "Kejuaraan"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("home_KejuaraanPelatih_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("home_KejuaraanPelatih_update", args=(self.pk,))



class SertifikatPelatih(models.Model):

    # Relationships
    pelatih = models.ForeignKey("home.Pelatih", on_delete=models.CASCADE)

    # Fields
    nama = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    foto = models.ImageField(upload_to="upload/images/")

    class Meta:
        verbose_name_plural = "Sertifikat"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("home_SertifikatPelatih_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("home_SertifikatPelatih_update", args=(self.pk,))



class Pelatih(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    nama = models.CharField(max_length=30)
    alamat = models.CharField(max_length=100)
    deskripsi = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    telp = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Pelatih"

    def __str__(self):
        return str(self.nama)

    def get_absolute_url(self):
        return reverse("home_Pelatih_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("home_Pelatih_update", args=(self.pk,))



class pengalaman(models.Model):

    # Relationships
    pelatih = models.ForeignKey("home.Pelatih", on_delete=models.CASCADE)

    # Fields
    keterangan = models.TextField(max_length=2000)
    foto = models.ImageField(upload_to="upload/images/")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    periode = models.CharField(max_length=20)
    tahun = models.CharField(max_length=4)
    nama_pengalaman = models.TextField(max_length=1000)

    class Meta:
        verbose_name_plural = "Pengalaman"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("home_pengalaman_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("home_pengalaman_update", args=(self.pk,))


class perkembangan(models.Model):
    
    #Fields
    kejuaraan = models.BigIntegerField()
    tahun = models.CharField(max_length=4)
    namaBidang = models.CharField(max_length=100, choices = BIDANG_CHOICES)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name_plural = "Perkembangan"
        
    def __str__(self):
        return str(self.pk)
    
    def get_absolute_url(self):
        return reverse("home_perkembangan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("home_perkembangan_update", args=(self.pk,))
    
class jenis_skill(models.Model):
    skill = models.CharField(max_length=1, choices = SKILL_CHOICES, default="1")
    pelatih = models.ForeignKey("home.Pelatih", on_delete=models.CASCADE)    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    rating = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    nama_skill = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Jenis Skill"

    def __str__(self):
        return str(self.pk)

    