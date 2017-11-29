from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Server, ServerIP

User = get_user_model()

class ServerSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Server
        fields = ('id', 'hostname', 'srv_type','tier', 'links', )

    def get_links(self,obj):
        request = self.context['request']
        return {
            'self': reverse('server-detail',
                            kwargs={'pk': obj.pk},request=request),
            'ips': reverse('serverip-list',
                           request=request) + '?server={}'.format(obj.pk),
        }

class ServerIPSerializer(serializers.ModelSerializer):
    
    #hostname = serializers.SlugRelatedField(
    #    slug_field = Server.hostname, required=False,allow_null=True,
    #    queryset=Server.objects.all())
    links = serializers.SerializerMethodField()

    class Meta:
        model = ServerIP
        fields = ('id','server_id','ip','links',)
        
    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('serverip-detail',kwargs={'pk': obj.pk}, request=request),
            'server': None
        }
        if obj.server_id:
            links['server'] = reverse('server-detail', kwargs={'pk': obj.server_id.pk}, request=request)
            
        return links


class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links', )

    def get_links(self,obj):
        request = self.context['request']
        return {
            'self': reverse('user-detail',
                            kwargs={User.USERNAME_FIELD: username},request=request),
        }
