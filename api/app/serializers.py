
from .models import  User
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ['id','username','password']