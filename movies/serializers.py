from .models import Movie
import datetime
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_rate(self, obj):
        reviews = obj.reviews.all()
        ratings = [review.stars for review in reviews if review.stars is not None]

        if ratings:
            return sum(ratings) / len(ratings)
        return 0

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("O título deve ter pelo menos 5 caracteres.")
        return value

    def validate_release_date(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("A data de lançamento não pode ser maior que a data atual.")
        return value
    
    def validate_actors(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("É necessário pelo menos dois atores.")
        return value
    
    def validate_resume(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("A sinopse deve ter pelo menos 10 caracteres.")
        if len(value) > 500:
            raise serializers.ValidationError("A sinopse não pode ser maior do que 500 caracteres.")
        return value