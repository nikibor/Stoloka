from rest_framework import serializers


class MapSerializer(serializers.Serializer):
    left_top_longitude = serializers.FloatField(required=True)
    left_top_latitude = serializers.FloatField(required=True)
    right_bottom_longitude = serializers.FloatField(required=True)
    right_bottom_latitude = serializers.FloatField(required=True)


class PlaceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()


class MapResponseSerializer(serializers.Serializer):
    places = serializers.ListField(child=PlaceSerializer())
