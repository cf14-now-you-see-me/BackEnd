from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by('id')
    serializer_class = PlaceSerializer

    @action(
        detail=True,
        methods=['GET'],
    )
    def recommend(self, request, pk=None):
        """
        Get similar places.
        """
        import re
        from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
        from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.cluster import KMeans
        
        # ambil semua Places
        places = Place.objects
        all_places = places.values()

        def preprocess(txt):
            """
            ubah semua kata dalam kalimat menjadi kata dasar
            """
            sf = StemmerFactory()
            swrf = StopWordRemoverFactory()
            stemmer = sf.create_stemmer()
            stop_remover = swrf.create_stop_word_remover()

            txt = re.sub(r'\r?\n', ' ', txt.strip())
            txt = re.sub(r'[0-9]+', '', txt)
            txt = txt.lower()
            txt = stemmer.stem(stop_remover.remove(txt))
            return txt
        
        deskripsi = [preprocess(x['long_description']) for x in all_places]
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(deskripsi)

        NUMBER_OF_CLUSTERS=6
        km = KMeans(n_clusters=NUMBER_OF_CLUSTERS)
        km.fit(X)

        p = get_object_or_404(Place, pk=pk) # tempat yang diminta

        found_idx = list(places.all()).index(p)
        selected_group = km.labels_[found_idx]
        similars = list(
            filter(lambda x: km.labels_[x[0]] == selected_group, enumerate(places.all()))
        )

        places = []
        for i in similars:
            place = PlaceSerializer(i[1], context={'request': request})
            place_data = place.data
            places.append(place_data)
        places = places[:5]
        
        return Response(places)

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all().order_by('id')
    serializer_class = AmenitySerializer

    @action(methods=['get'], detail=False, url_path='by-place/(?P<place_id>\d+)', url_name='by_place')
    def get_by_place(self, request, place_id, pk=None):
        filtered = AmenitySerializer(
            Amenity.objects.filter(near=place_id).all(),
            many=True,
            context={'request': request}
        )
        return Response(filtered.data)