from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Server, ServerIP,HRBL_App, Server_App

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
            'apps': reverse('server_app-list',
                           request=request) + '?server_app={}'.format(obj.pk),
        }

class ServerIPSerializer(serializers.ModelSerializer):
    
   # hostname = serializers.SlugRelatedField(
   #     slug_field = Server.hostname, required=False,allow_null=True,
   #     queryset=Server.objects.all())
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

class HRBL_AppSerializer(serializers.ModelSerializer):
    
    links = serializers.SerializerMethodField()

    class Meta:
        model = HRBL_App
        fields = ('id','name','description','links',)
        
    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('hrbl_app-detail',kwargs={'pk': obj.pk}, request=request),
        }
        return links

class Server_AppSerializer(serializers.ModelSerializer):
    
    links = serializers.SerializerMethodField()

    class Meta:
        model = Server_App
        fields = ('id','server_id','app_id','notes','links',)
        
    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('server_app-detail',kwargs={'pk': obj.pk}, request=request),
            'server': None,
            'app': None,
        }
        if obj.server_id:
            links['server'] = reverse('server-detail', kwargs={'pk': obj.server_id.pk}, request=request)
        if obj.app_id:
            links['app'] = reverse('hrbl_app-detail', kwargs={'pk': obj.app_id.pk}, request=request)
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
