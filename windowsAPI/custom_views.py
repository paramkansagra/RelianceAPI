from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from .serializers import (
    OSNameSerializer,
    HostNameSerializer,
    OSVersionSerializer,
    BootDeviceSerializer,
    DomainSerializer,
    OSBuildTypeSerializer,
    OSConfigSerializer,
    RegOwnerSerializer,
    SystemBootTimeSerializer,
    SystemModelSerializer,
    SystemTypeSerializer,
    WindowsDirSerializer,
    LogonServerSerializer,
)

from datetime import datetime

class ImportDataViewSet(ViewSet):

    @action(methods=["POST"],detail=False)
    def import_data(self,request):

        def getDateTime(system_time):
            date = list(map(int,system_time[0][:len(system_time[0])-1].split("/"))) # format is month day year
            date[0] , date[1] = date[1] , date[0] # format is day month
            time = list(map(int,system_time[1].split(":"))) # format is hh:mm:ss

            if(system_time[2] == "PM"):
                time[0] = (12 + time[0])%24
            print(time)

            finalDateTime = datetime(date[-1],date[-2],date[-3],time[0],time[1],time[2])
            return finalDateTime

        
        data = request.data


        host_name_data = {"host_name" : data["Host Name"]}
        os_name_data = {"os_name" : data["OS Name"] , **host_name_data}
        os_version_data = {"os_version" : data["OS Version"] , **host_name_data}
        boot_device_data = {"boot_device" : data["Boot Device"] , **host_name_data}
        domain_data = {"domain" : data["Domain"] , **host_name_data}
        os_build_type_data = {"os_build_type" : data["OS Build Type"] , **host_name_data}
        os_config_data = {"os_config" : data["OS Configuration"] , **host_name_data}
        reg_owner_data = {"reg_owner" : data["Registered Owner"] , **host_name_data}
        system_model_data = {"system_model" : data["System Model"] , **host_name_data}
        system_type_data = {"system_type" : data["System Type"] , **host_name_data}
        windows_dir_data = {"windows_dir" : data["Windows Directory"] , **host_name_data}
        logon_server_data = {"logon_server" : data["Logon Server"] , **host_name_data}
        print("hello world")
        system_boot_date_time = getDateTime(system_time=data["System Boot Time"].split(" "))
        system_boot_data = {"system_boot_time" : system_boot_date_time, **host_name_data}

        host_name_serializer = HostNameSerializer(data=host_name_data)
        if(host_name_serializer.is_valid()):
            host_name_serializer.save()
            print("Host name saved")
        else:
            error_message = host_name_serializer.errors["host_name"][0]
            if(error_message != "host name with this host name already exists."):
                return Response(host_name_serializer.errors,status=400)

        os_name_serializer = OSNameSerializer(data=os_name_data)
        if(os_name_serializer.is_valid()):
            os_name_serializer.save()
            print("os name saved")
        else:
            error_message = os_name_serializer.errors["os_name"][0]
            if(error_message != "os name with this os name already exists."):
                return Response(os_name_serializer.errors,status=400)
        
        os_version_serializer = OSVersionSerializer(data=os_version_data)
        if(os_version_serializer.is_valid()):
            os_version_serializer.save()
            print("os version saved")
        else:
            error_message = os_version_serializer.errors["os_version"][0]
            if(error_message != "os version with this os version already exists."):
                return Response(os_version_serializer.errors,status=400)

        boot_device_serializer = BootDeviceSerializer(data=boot_device_data)
        if(boot_device_serializer.is_valid()):
            boot_device_serializer.save()
        else:
            error_message = boot_device_serializer.errors["boot_device"][0]
            if(error_message != "boot device with this boot device already exists."):
                return Response(boot_device_serializer.errors,status=400)
        
        domain_serializer = DomainSerializer(data = domain_data)
        if(domain_serializer.is_valid()):
            domain_serializer.save()
            print("domain data saved")
        else:
            error_message = domain_serializer.errors["domain"][0]
            if(error_message != "domain with this domain already exists."):
                return Response(domain_serializer.errors,status=400)
        
        os_build_type_serializer = OSBuildTypeSerializer(data = os_build_type_data)
        if(os_build_type_serializer.is_valid()):
            os_build_type_serializer.save()
            print("os build type saved")
        else:
            error_message = os_build_type_serializer.errors["os_build_type"][0]
            if(error_message != "os build type with this os build type already exists."):
                return Response(os_build_type_serializer.errors,status=400)
        
        os_config_serializer = OSConfigSerializer(data = os_config_data)
        if(os_config_serializer.is_valid()):
            os_config_serializer.save()
            print("os config data saved")
        else:
            error_message = os_config_serializer.errors["os_config"][0]
            if(error_message != "os config with this os config already exists."):
                return Response(os_config_serializer.errors,status=400)
        
        reg_owner_serializer = RegOwnerSerializer(data = reg_owner_data)
        if(reg_owner_serializer.is_valid()):
            reg_owner_serializer.save()
            print("reg owner data saved")
        else:
            error_message = reg_owner_serializer.errors["reg_owner"][0]
            if(error_message != "reg owner with this reg owner already exists."):
                return Response(reg_owner_serializer.errors,status=400)

        system_model_serializer = SystemModelSerializer(data = system_model_data)
        if(system_model_serializer.is_valid()):
            system_model_serializer.save()
            print("system model data saved")
        else:
            error_message = system_model_serializer.errors["system_model"][0]
            if(error_message != "system model with this system model already exists."):
                return Response(system_model_serializer.errors,status=400)
        
        system_type_serializer = SystemTypeSerializer(data = system_type_data)
        if(system_type_serializer.is_valid()):
            system_type_serializer.save()
            print("system_type data saved")
        else:
            error_message = system_type_serializer.errors["system_type"][0]
            if(error_message != "system type with this system type already exists."):
                return Response(system_type_serializer.errors,status=400)
        
        windows_dir_serializer = WindowsDirSerializer(data = windows_dir_data)
        if(windows_dir_serializer.is_valid()):
            windows_dir_serializer.save()
            print("windows_dir data saved")
        else:
            error_message = windows_dir_serializer.errors["windows_dir"][0]
            if(error_message != "windows dir with this windows dir already exists."):
                return Response(windows_dir_serializer.errors,status=400)
        
        logon_server_serializer = LogonServerSerializer(data = logon_server_data)
        if(logon_server_serializer.is_valid()):
            logon_server_serializer.save()
            print("logon_server data saved")
        else:
            error_message = logon_server_serializer.errors["logon_server"][0]
            if(error_message != "logon server with this logon server already exists."):
                return Response(logon_server_serializer.errors,status=400)
        
        system_boot_serializer = SystemBootTimeSerializer(data = system_boot_data)
        if(system_boot_serializer.is_valid()):
            system_boot_serializer.save()
            print("system_boot data saved")
        else:
            error_message = system_boot_serializer.errors["system_boot_time"][0]
            if(error_message != "system boot with this system boot already exists."):
                return Response(logon_server_serializer.errors,status=400)

        return Response("All data saved" , status=200)