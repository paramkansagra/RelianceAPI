from rest_framework import serializers
from .models import HostName,OSName,OSVersion,BIOSVersion,BootDevice,Domain,LogonServer,OSBuildType
from .models import OSConfig,RegOwner,SystemBootTime,SystemModel,SystemType,WindowsDir

class HostNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostName
        fields = ["host_name"]

class OSNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSName
        fields = ["os_name","host_name"]

class OSVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSVersion
        fields = ["os_version","host_name"]

class BIOSVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BIOSVersion
        fields = ["bios_version","host_name"]

class BootDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootDevice
        fields = ["boot_device","host_name"]

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["domain","host_name"]

class LogonServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogonServer
        fields = ["logon_server","host_name"]

class OSBuildTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSBuildType
        fields = ["os_build_type","host_name"]

class OSConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSConfig
        fields = ["os_config","host_name"]

class RegOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegOwner
        fields = ["reg_owner","host_name"]

class SystemBootTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemBootTime
        fields = ["system_boot_time","host_name"]

class SystemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemModel
        fields = ["system_model","host_name"]

class SystemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemType
        fields = ["system_type","host_name"]

class WindowsDirSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsDir
        fields = ["windows_dir","host_name"]