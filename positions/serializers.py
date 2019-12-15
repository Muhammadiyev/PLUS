from rest_framework import serializers
from .models import Global, Lacal


class GlobalSerializers(serializers.ModelSerializer):

    class Meta:
        model = Global
        fields = ('id', 'global_position', 'user')


class LacalSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lacal
        fields = ('id', 'local_position', 'user')