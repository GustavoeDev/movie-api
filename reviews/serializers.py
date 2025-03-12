from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_comment(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('O comentário deve ter pelo menos 5 caracteres.')
        if len(value) > 400:
            raise serializers.ValidationError('O comentário deve ter no máximo 400 caracteres.')
        return value