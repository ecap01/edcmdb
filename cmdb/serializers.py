from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Server, ServerIP

User = get_user_model()

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'hostname', 'srv_type','tier', )

class ServerIPSerializer(serializers.ModelSerializer):
    hostname = serializers.SlugRelatedField(
        slug_field = Server.HOSTNAME_FIELD, required=False, allow_null=True,
        queryset=Server.objects.all())
    class Meta:
        model = ServerIP
        fields = ('id','hostname','ip',)
        
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', )