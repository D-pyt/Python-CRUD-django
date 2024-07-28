from rest_framework import serializers
from stars.models import Star

 
class StarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    star_name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    star_constellation = serializers.CharField(max_length=50, required=False)
    star_type = serializers.CharField(max_length=50, required=False)
    star_distance = serializers.CharField(max_length=25,required=False)
    star_mass = serializers.CharField(max_length=25, required=False)
    star_temperature = serializers.CharField(max_length=25, required=False)
    star_period = serializers.CharField(max_length=25, required=False)
    star_turn_speed = serializers.CharField(max_length=25,required=False)

    def create(self, validated_data):
        return Star.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.star_name = validated_data.get('name', instance.star_name)
        instance.star_constellation = validated_data.get('constellation', instance.star_constellation)
        instance.star_type = validated_data.get('type', instance.star_type)
        instance.star_distance = validated_data.get('distance', instance.star_distance)
        instance.star_mass = validated_data.get('mass', instance.star_mass)
        instance.star_temperature = validated_data.get('temperature', instance.star_temperature)
        instance.star_period = validated_data.get('period', instance.star_period)
        instance.star_turn_speed = validated_data.get('turn_speed', instance.star_turn_speed)
        instance.save()
        return instance
