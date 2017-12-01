from django.contrib.auth import get_user_model

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import authentication, permissions, viewsets, filters

from .models import Server, ServerIP, HRBL_App, Server_App
from .serializers import ServerSerializer, ServerIPSerializer, HRBL_AppSerializer, Server_AppSerializer, UserSerializer  

User = get_user_model() 

class DefaultsMixin(object):
    ''' Default setting for view authentication, permissions, filtering and pagination. '''
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        #filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

class ServerViewSet(DefaultsMixin, viewsets.ModelViewSet):
    ''' API endpoint for listing and creating Servers. '''

    queryset = Server.objects.order_by('hostname')
    serializer_class = ServerSerializer
    search_fields = ('hostname',)
    ordering_fields = ('hostname',)

class ServerIPViewSet(DefaultsMixin, viewsets.ModelViewSet):
    ''' API endpoint for listing and creating Server IPs  '''
    queryset = ServerIP.objects.all()
    serializer_class = ServerIPSerializer
    search_fields = ('ip',)
    ordering_fields = ('ip',)

class HRBL_AppViewSet(DefaultsMixin, viewsets.ModelViewSet):
    ''' API endpoint for listing and creating Herbalife Apps '''
    queryset = HRBL_App.objects.all()
    serializer_class = HRBL_AppSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class Server_AppViewSet(DefaultsMixin, viewsets.ModelViewSet):
    ''' API endpoint for listing and creating Server Apps  '''
    queryset = Server_App.objects.all()
    serializer_class = Server_AppSerializer
    search_fields = ('notes',)

class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    ''' API endpoint for listing Users '''
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD,)
