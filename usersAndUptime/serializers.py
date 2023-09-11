from rest_framework import serializers
from .models import HostName, Users, Uptime


class HostNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostName
        fields = ["host_name"]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["host_name", "user_name", "group_name"]


class UptimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uptime
        fields = ["host_name" , "uptime"]
