from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from rest_framework import viewsets, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return HttpResponse("index")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

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
        
        deskripsi = [preprocess(x['description']) for x in all_places]
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(deskripsi)

        NUMBER_OF_CLUSTERS=3
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
            packages = [PackageSerializer(j, context={'request':request}).data for j in Package.objects.filter(place=i[1])]
            for i in packages:
                del i['id']
                del i['place']
            place_data['packages'] = packages
            places.append(place_data)
        
        return Response(places)

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = []
