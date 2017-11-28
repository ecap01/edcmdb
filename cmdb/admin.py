from django.contrib import admin
from .models import Server, ServerIP, HRBL_App, Server_App

admin.site.register(Server)
admin.site.register(ServerIP)
admin.site.register(HRBL_App)
admin.site.register(Server_App)


