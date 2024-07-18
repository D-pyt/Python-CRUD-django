from rest_framework import serializers
from stars.models import Star

class StarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    star_name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    star_constellation = serializers.CharField(style={'base_template': 'textarea.html'})
    star_type = serializers.CharField(style={'base_template': 'textarea.html'})
    star_distance = serializers.CharField(max_length=25)
    star_mass = serializers.CharField(max_length=25)
    star_temperature = serializers.CharField(max_length=25)
    star_period = serializers.CharField(max_length=25)
    star_turn_speed = serializers.CharField(max_length=25)

    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Star.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.star_name = validated_data.get('star_name', instance.star_name)
        instance.star_constellation = validated_data.get('star_constellation', instance.star_constellation)
        instance.star_type = validated_data.get('star_type', instance.star_type)
        instance.star_distance = validated_data.get('star_distance', instance.star_distance)
        instance.star_mass = validated_data.get('star_mass', instance.star_mass)
        instance.star_temperature = validated_data.get('star_temperature', instance.star_temperature)
        instance.star_period = validated_data.get('star_period', instance.star_period)
        instance.star_turn_speed = validated_data.get('star_turn_speed', instance.star_turn_speed)
        instance.save()
        return instance