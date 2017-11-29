from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import authentication, permissions, viewsets

from .models import Server
from .serializers import ServerSerializer

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

class ServerViewSet(viewsets.ModelViewSet):
    ''' API endpoint for listing and creating Servers. '''
    
    queryset = Server.objects.order_by('hostname')
    serializer_class =  ServerSerializer
    
def index(request):
    return HttpResponse("Hi, You are in the cmdb index")
