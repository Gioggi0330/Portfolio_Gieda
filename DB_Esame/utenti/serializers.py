from rest_framework import serializers
from .models import Utente

class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = ['nome', 'cognome','email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Utente.objects.create(**validated_data)
        user.set_password(password)  
        user.save()
        return user
