from django.shortcuts import render

from .models import Language, PlaceName, Community, Champion
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import (
    LanguageGeoSerializer,
    LanguageSerializer,
    LanguageDetailSerializer,
    PlaceNameGeoSerializer,
    CommunitySerializer,
    CommunityDetailSerializer,
    ChampionSerializer,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class LanguageList(generics.ListAPIView):
    """
    API endpoint that allows languages to be viewed or edited.
    """

    queryset = Language.objects.filter(geom__isnull=False)
    serializer_class = LanguageSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        queryset = self.get_queryset()
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)


class LanguageDetail(generics.RetrieveAPIView):
    serializer_class = LanguageDetailSerializer
    queryset = Language.objects.all()


class LanguageGeoList(generics.ListAPIView):
    queryset = Language.objects.filter(geom__isnull=False)
    serializer_class = LanguageGeoSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        queryset = self.get_queryset()
        serializer = LanguageGeoSerializer(queryset, many=True)
        return Response(serializer.data)


class CommunityList(generics.ListAPIView):

    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        queryset = self.get_queryset()
        if "lang" in request.GET:
            queryset = queryset.filter(
                languages=Language.objects.get(pk=request.GET.get("lang"))
            )
        serializer = CommunitySerializer(queryset, many=True)
        return Response(serializer.data)


class CommunityDetail(generics.RetrieveAPIView):
    serializer_class = CommunityDetailSerializer
    queryset = Community.objects.all()


class PlaceNameGeoList(generics.ListAPIView):

    queryset = PlaceName.objects.all()
    serializer_class = PlaceNameGeoSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        queryset = self.get_queryset()
        if "lang" in request.GET:
            lang = Language.objects.get(pk=int(request.GET["lang"]))
            print(lang.geom)
            queryset = queryset.filter(point__intersects=lang.geom)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

