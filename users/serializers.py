from rest_framework import serializers
from .models import User

class UserLocalSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',
        'first_name','last_name',
        'image','years_old','phone',
        'created')

class UserGlobalSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',
        'first_name','last_name',
        'image','years_old','phone',
        'created')