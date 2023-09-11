from django.db import models


# Create your models here.
class HostName(models.Model):
    host_name = models.CharField(max_length=255, primary_key=True)


class Users(models.Model):
    host_name = models.ForeignKey(HostName, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255 , unique=True)
    group_name = models.CharField(max_length=255 )


class Uptime(models.Model):
    host_name = models.ForeignKey(HostName, on_delete=models.CASCADE)
    uptime = models.DateTimeField(unique=True)