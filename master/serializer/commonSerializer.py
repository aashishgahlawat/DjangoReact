from rest_framework import serializers
from ..models import MasterCountry, MasterState, MasterCity


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCountry
        fields = '__all__'
        # exclude = ''
        # depth = 1


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterState
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCity
        fields = '__all__'
