from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from django.shortcuts import render

def pelatih(request, pk):
    pelatih = models.Pelatih.objects.get(pk=pk)
    context = {"pelatih": pelatih}
    return render(request, "pelatih.html", context)
    
class PelatihListView(generic.ListView):
    model = models.Pelatih
    form_class = forms.PelatihForm


class PelatihCreateView(generic.CreateView):
    model = models.Pelatih
    form_class = forms.PelatihForm


class PelatihDetailView(generic.DetailView):
    model = models.Pelatih
    form_class = forms.PelatihForm


class PelatihUpdateView(generic.UpdateView):
    model = models.Pelatih
    form_class = forms.PelatihForm
    pk_url_kwarg = "pk"


class PelatihDeleteView(generic.DeleteView):
    model = models.Pelatih
    success_url = reverse_lazy("home_Pelatih_list")

class KejuaraanPelatihListView(generic.ListView):
    model = models.KejuaraanPelatih
    form_class = forms.KejuaraanPelatihForm


class KejuaraanPelatihCreateView(generic.CreateView):
    model = models.KejuaraanPelatih
    form_class = forms.KejuaraanPelatihForm


class KejuaraanPelatihDetailView(generic.DetailView):
    model = models.KejuaraanPelatih
    form_class = forms.KejuaraanPelatihForm


class KejuaraanPelatihUpdateView(generic.UpdateView):
    model = models.KejuaraanPelatih
    form_class = forms.KejuaraanPelatihForm
    pk_url_kwarg = "pk"


class KejuaraanPelatihDeleteView(generic.DeleteView):
    model = models.KejuaraanPelatih
    success_url = reverse_lazy("home_KejuaraanPelatih_list")


class SertifikatPelatihListView(generic.ListView):
    model = models.SertifikatPelatih
    form_class = forms.SertifikatPelatihForm


class SertifikatPelatihCreateView(generic.CreateView):
    model = models.SertifikatPelatih
    form_class = forms.SertifikatPelatihForm


class SertifikatPelatihDetailView(generic.DetailView):
    model = models.SertifikatPelatih
    form_class = forms.SertifikatPelatihForm


class SertifikatPelatihUpdateView(generic.UpdateView):
    model = models.SertifikatPelatih
    form_class = forms.SertifikatPelatihForm
    pk_url_kwarg = "pk"


class SertifikatPelatihDeleteView(generic.DeleteView):
    model = models.SertifikatPelatih
    success_url = reverse_lazy("home_SertifikatPelatih_list")


class jenis_skillListView(generic.ListView):
    model = models.jenis_skill
    form_class = forms.jenis_skillForm


class jenis_skillCreateView(generic.CreateView):
    model = models.jenis_skill
    form_class = forms.jenis_skillForm


class jenis_skillDetailView(generic.DetailView):
    model = models.jenis_skill
    form_class = forms.jenis_skillForm


class jenis_skillUpdateView(generic.UpdateView):
    model = models.jenis_skill
    form_class = forms.jenis_skillForm
    pk_url_kwarg = "pk"


class jenis_skillDeleteView(generic.DeleteView):
    model = models.jenis_skill
    success_url = reverse_lazy("home_jenis_skill_list")


class pengalamanListView(generic.ListView):
    model = models.pengalaman
    form_class = forms.pengalamanForm


class pengalamanCreateView(generic.CreateView):
    model = models.pengalaman
    form_class = forms.pengalamanForm


class pengalamanDetailView(generic.DetailView):
    model = models.pengalaman
    form_class = forms.pengalamanForm


class pengalamanUpdateView(generic.UpdateView):
    model = models.pengalaman
    form_class = forms.pengalamanForm
    pk_url_kwarg = "pk"


class pengalamanDeleteView(generic.DeleteView):
    model = models.pengalaman
    success_url = reverse_lazy("home_pengalaman_list")

class perkembanganListView(generic.ListView):
    model = models.perkembangan
    form_class = forms.perkembanganForm


class perkembanganCreateView(generic.CreateView):
    model = models.perkembangan
    form_class = forms.perkembanganForm


class perkembanganDetailView(generic.DetailView):
    model = models.perkembangan
    form_class = forms.perkembanganForm


class perkembanganUpdateView(generic.UpdateView):
    model = models.perkembangan
    form_class = forms.perkembanganForm
    pk_url_kwarg = "pk"


class perkembanganDeleteView(generic.DeleteView):
    model = models.perkembangan
    success_url = reverse_lazy("home_perkembangan_list")