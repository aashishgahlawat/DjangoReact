from rest_framework import viewsets, mixins, status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import MasterCountry, MasterCity, MasterState
from master.serializer.commonSerializer import CountrySerializer, StateSerializer, CitySerializer
from rest_framework.views import Response, APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Can list, retrieve
    """
    queryset = MasterCountry.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

# class CountryViewSet(viewsets.ModelViewSet):
#     """
#     Can list, retrieve, add, update and delete (CRUD operations)
#     """
#     queryset = MasterCountry.objects.all()
#     serializer_class = CountrySerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (TokenAuthentication,)


"""
class GetCountry(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = MasterCountry.objects.all()
    serializer_class = CountrySerializer
    permission_classes = AllowAny
"""

# class GetCountry(viewsets.ViewSet):
#
#     def list(self, request):
#         """
#         fetch list of all countries
#         :param request:
#         :return:
#         """
#         country = MasterCountry.objects.all()
#         serialized_country = StateSerializer(country, many=True)
#         return Response(serialized_country.data, status=status.HTTP_200_OK)
#
#     def retrieve(self, request, pk=None):
#         """
#         fetch individual country details
#         :param request:
#         :param pk:
#         :return:
#         """
#         queryset = MasterCountry.objects.all()
#         country = get_object_or_404(queryset, pk=pk)
#         serialized_country = StateSerializer(country)
#         return Response(serialized_country.data)

"""

class GetCountryList(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = MasterCountry.objects.all()
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetCountryDetails(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = MasterCountry.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'
    
    def get(self, request, id):
        return self.retrieve(self, request, id=id)

"""

"""

class GetCountryList(APIView):
    
    def get(self, request):
        country = MasterCountry.objects.all()
        serialized_country = CountrySerializer(country, many=True)
        return Response(serialized_country.data, status=status.HTTP_200_OK)


class GetCountryDetail(APIView):

    def get(self, request, id):
        try: 
            country = MasterCountry.objects.get(id=id)
        except MasterCountry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_country = CountrySerializer(country, many=False)
        return Response(serialized_country.data, status=status.HTTP_200_OK)

"""

"""

@api_view(['GET', ])
def get_country_list(request):
    if request.method == 'GET':
        country = MasterCountry.objects.all()
        serialized_country = CountrySerializer(country, many=True)
        return Response(serialized_country.data, status=status.HTTP_200_OK)
    

@api_view(['GET', ]) 
def get_country_details(request, id):
    if request.method == 'GET':
        try:
            country = MasterCountry.objects.get(id=id)
        except MasterCountry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_country = CountrySerializer(country, many=False)
        return Response(serialized_country.data, status=status.HTTP_200_OK)

"""
