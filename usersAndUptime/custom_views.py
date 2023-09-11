from dateutil import parser

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from .serializers import (
    HostNameSerializer,
    UptimeSerializer,
    UsersSerializer,
)

from datetime import datetime

class ImportDataViewSet(ViewSet):

    @action(methods=["POST"],detail=False)
    def import_data(self,request):

        def getDateTime(system_time):
            date = parser.isoparse(system_time)

            return date

        
        data = request.data


        host_name_data = {"host_name" : data["host_name"]}

        host_name_serializer = HostNameSerializer(data=host_name_data)
        if(host_name_serializer.is_valid()):
            host_name_serializer.save()
        
        group_seralizer = [UsersSerializer(data = group_data) for group_data in data.get("groups",[])]
        if(all(seralizer.is_valid() for seralizer in group_seralizer)):
            for group_instance in group_seralizer:
                group_instance.save()
                print("saved")
        
        uptime_data = {"uptime":getDateTime(data["uptime"]) , "host_name" : data["host_name"]}
        print(uptime_data)

        uptime_seralizer = UptimeSerializer(data=uptime_data)

        if(uptime_seralizer.is_valid()):
            uptime_seralizer.save()

        return Response("All data saved" , status=200)