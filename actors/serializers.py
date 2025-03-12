from rest_framework import serializers
import datetime
from .models import Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_date_of_birth(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Data de nascimento não pode ser maior que a data atual.")
        return value
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value