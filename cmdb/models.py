from django.db import models

class Server(models.Model):
    SRV_TYPES = (
        ('P', 'Physical'),
        ('V', 'Virtual'),
        ('A', 'Appliance'),
    )

    SRV_TIERS = (
        ('AP','Application - Apache, Weblogic, etc'),
        ('CM','Concurrent Manager'),
        ('DB','Database'),
        ('PX','Proxy'),
        ('NA','Not Applicable'),
    )
    hostname = models.CharField(max_length=200)
    srv_type = models.CharField(max_length=1, choices=SRV_TYPES)
    tier = models.CharField(max_length=2, choices=SRV_TIERS)
    

class ServerIP(models.Model):
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(protocol='IPv4')

class HRBL_App(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=255)

class Server_App(models.Model):
    server_id = models.ForeignKey(Server)
    app_id = models.ForeignKey(HRBL_App)
    notes = models.CharField(max_length=255)


