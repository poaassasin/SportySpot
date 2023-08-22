from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Pelatih", api.PelatihViewSet)
router.register("KejuaraanPelatih", api.KejuaraanPelatihViewSet)
router.register("SertifikatPelatih", api.SertifikatPelatihViewSet)
router.register("jenis_skill", api.jenis_skillViewSet)
router.register("perkembangan", api.perkembanganViewSet)
router.register("pengalaman", api.pengalamanViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("home/Pelatih/", views.PelatihListView.as_view(), name="home_Pelatih_list"),
    path("home/Pelatih/create/", views.PelatihCreateView.as_view(), name="home_Pelatih_create"),
    path("home/Pelatih/detail/<int:pk>/", views.PelatihDetailView.as_view(), name="home_Pelatih_detail"),
    path("home/Pelatih/update/<int:pk>/", views.PelatihUpdateView.as_view(), name="home_Pelatih_update"),
    path("home/Pelatih/delete/<int:pk>/", views.PelatihDeleteView.as_view(), name="home_Pelatih_delete"),
    path("home/skill/", views.skillListView.as_view(), name="home_skill_list"),
    path("home/KejuaraanPelatih/", views.KejuaraanPelatihListView.as_view(), name="home_KejuaraanPelatih_list"),
    path("home/KejuaraanPelatih/create/", views.KejuaraanPelatihCreateView.as_view(), name="home_KejuaraanPelatih_create"),
    path("home/KejuaraanPelatih/detail/<int:pk>/", views.KejuaraanPelatihDetailView.as_view(), name="home_KejuaraanPelatih_detail"),
    path("home/KejuaraanPelatih/update/<int:pk>/", views.KejuaraanPelatihUpdateView.as_view(), name="home_KejuaraanPelatih_update"),
    path("home/KejuaraanPelatih/delete/<int:pk>/", views.KejuaraanPelatihDeleteView.as_view(), name="home_KejuaraanPelatih_delete"),
    path("home/SertifikatPelatih/", views.SertifikatPelatihListView.as_view(), name="home_SertifikatPelatih_list"),
    path("home/SertifikatPelatih/create/", views.SertifikatPelatihCreateView.as_view(), name="home_SertifikatPelatih_create"),
    path("home/SertifikatPelatih/detail/<int:pk>/", views.SertifikatPelatihDetailView.as_view(), name="home_SertifikatPelatih_detail"),
    path("home/SertifikatPelatih/update/<int:pk>/", views.SertifikatPelatihUpdateView.as_view(), name="home_SertifikatPelatih_update"),
    path("home/SertifikatPelatih/delete/<int:pk>/", views.SertifikatPelatihDeleteView.as_view(), name="home_SertifikatPelatih_delete"),
    path("home/jenis_skill/", views.jenis_skillListView.as_view(), name="home_jenis_skill_list"),
    path("home/jenis_skill/create/", views.jenis_skillCreateView.as_view(), name="home_jenis_skill_create"),
    path("home/jenis_skill/detail/<int:pk>/", views.jenis_skillDetailView.as_view(), name="home_jenis_skill_detail"),
    path("home/jenis_skill/update/<int:pk>/", views.jenis_skillUpdateView.as_view(), name="home_jenis_skill_update"),
    path("home/jenis_skill/delete/<int:pk>/", views.jenis_skillDeleteView.as_view(), name="home_jenis_skill_delete"),
    path("home/pengalaman/", views.pengalamanListView.as_view(), name="home_pengalaman_list"),
    path("home/pengalaman/create/", views.pengalamanCreateView.as_view(), name="home_pengalaman_create"),
    path("home/pengalaman/detail/<int:pk>/", views.pengalamanDetailView.as_view(), name="home_pengalaman_detail"),
    path("home/pengalaman/update/<int:pk>/", views.pengalamanUpdateView.as_view(), name="home_pengalaman_update"),
    path("home/pengalaman/delete/<int:pk>/", views.pengalamanDeleteView.as_view(), name="home_pengalaman_delete"),
    path("home/perkembangan/", views.perkembanganListView.as_view(), name="home_perkembangan_list"),
    path("home/perkembangan/create/", views.perkembanganCreateView.as_view(), name="home_perkembangan_create"),
    path("home/perkembangan/detail/<int:pk>/", views.perkembanganDetailView.as_view(), name="home_perkembangan_detail"),
    path("home/perkembangan/update/<int:pk>/", views.perkembanganUpdateView.as_view(), name="home_perkembangan_update"),
    path("home/perkembangan/delete/<int:pk>/", views.perkembanganDeleteView.as_view(), name="home_perkembangan_delete"),
)
