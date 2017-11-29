from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import reverse
from .models import Server, ServerIP

User = get_user_model()

class ServerSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')

    class Meta:
        model = Server
        fields = ('id', 'hostname', 'srv_type','tier', 'links', )

    def get_links(self,obj):
        request = self.context['server-detail']
        return {
            'self': reverse('hostname',
                            kwargs={'pk':obj.pk},request=request),
        }

class ServerIPSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    hostname = serializers.SlugRelatedField(
        slug_field = Server.HOSTNAME_FIELD, required=False, allow_null=True,
        queryset=Server.objects.all())

    class Meta:
        model = ServerIP
        fields = ('id','hostname','ip','links',)
        
    def get_links(self,obj):
        request = self.context['request']
        return {
            'self': reverse('serverip-detail',
                            kwargs={'pk':obj.pk},request=request),
        }

class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links', )

    def get_links(self,obj):
        request = self.context['request']
        return {
            'self': reverse('user-detail',
                            kwargs={User.USERNAME_FIELD:username},request=request),
        }
