from rest_framework import serializers
from .models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value