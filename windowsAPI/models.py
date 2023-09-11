from django.db import models

# Create your models here.

class HostName(models.Model):
    host_name = models.CharField(max_length=255,primary_key=True)

class OSName(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    os_name = models.CharField(max_length=255,unique=True)

class OSVersion(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    os_version = models.CharField(max_length=255,unique=True)

class OSConfig(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    os_config = models.CharField(max_length=255,unique=True)

class OSBuildType(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    os_build_type = models.CharField(max_length=255,unique=True)

class RegOwner(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    reg_owner = models.CharField(max_length=255,unique=True)

class SystemBootTime(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    system_boot_time = models.DateTimeField(unique=True)

class SystemModel(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    system_model = models.CharField(max_length=255,unique=True)

class SystemType(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    system_type = models.CharField(max_length=255,unique=True)

class BIOSVersion(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    bios_version = models.CharField(max_length=255,unique=True)

class WindowsDir(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    windows_dir = models.CharField(max_length=255,unique=True)

class BootDevice(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    boot_device = models.CharField(max_length=255,unique=True)

class Domain(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    domain = models.CharField(max_length=255,unique=True)

class LogonServer(models.Model):
    host_name = models.ForeignKey(HostName,on_delete=models.CASCADE)
    logon_server = models.CharField(max_length=255,unique=True)