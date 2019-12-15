from rest_framework import serializers
from .models import Global, Local
from users.serializers import UserGlobalSerializers, UserLocalSerializers

class GlobalSerializers(serializers.ModelSerializer):

    class Meta:
        model = Global
        fields = ('id', 'global_position', 'global_user')


class LacalSerializers(serializers.ModelSerializer):

    class Meta:
        model = Local
        fields = ('id', 'local_position', 'local_user')


class GlobalSerializersAll(serializers.ModelSerializer):
    global_user = UserGlobalSerializers(read_only=True)

    class Meta:
        model = Global
        fields =  ['id', 'global_position','created','global_user']


class LacalSerializersAll(serializers.ModelSerializer):
    local_user = UserLocalSerializers(read_only=True)
    
    class Meta:
        model = Local
        fields = '__all__'