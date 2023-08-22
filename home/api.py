from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PelatihViewSet(viewsets.ModelViewSet):
    """ViewSet for the Pelatih class"""

    queryset = models.Pelatih.objects.all()
    serializer_class = serializers.PelatihSerializer
    permission_classes = [permissions.IsAuthenticated]


class skillViewSet(viewsets.ModelViewSet):
    """ViewSet for the skill class"""

    queryset = models.skill.objects.all()
    serializer_class = serializers.skillSerializer
    permission_classes = [permissions.IsAuthenticated]


class KejuaraanPelatihViewSet(viewsets.ModelViewSet):
    """ViewSet for the KejuaraanPelatih class"""

    queryset = models.KejuaraanPelatih.objects.all()
    serializer_class = serializers.KejuaraanPelatihSerializer
    permission_classes = [permissions.IsAuthenticated]


class SertifikatPelatihViewSet(viewsets.ModelViewSet):
    """ViewSet for the SertifikatPelatih class"""

    queryset = models.SertifikatPelatih.objects.all()
    serializer_class = serializers.SertifikatPelatihSerializer
    permission_classes = [permissions.IsAuthenticated]


class jenis_skillViewSet(viewsets.ModelViewSet):
    """ViewSet for the jenis_skill class"""

    queryset = models.jenis_skill.objects.all()
    serializer_class = serializers.jenis_skillSerializer
    permission_classes = [permissions.IsAuthenticated]


class pengalamanViewSet(viewsets.ModelViewSet):
    """ViewSet for the pengalaman class"""

    queryset = models.pengalaman.objects.all()
    serializer_class = serializers.pengalamanSerializer
    permission_classes = [permissions.IsAuthenticated]

class perkembanganViewSet(viewsets.ModelViewSet):
    """ViewSet for the perkembangan class"""

    queryset = models.perkembangan.objects.all()
    serializer_class = serializers.perkembanganSerializer
    permission_classes = [permissions.IsAuthenticated]