from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Student,Blog


class studentserializer(ModelSerializer):
    result=serializers.SerializerMethodField()
    grade=serializers.SerializerMethodField()
    class Meta:
        model=Student
        fields=[f.name for f in Student._meta.fields]+["result","grade"]
    def validate_last_name(self,value):
        if value=="test":
          raise  serializers.ValidationError("Test surname is not allowed")
        return value
    def get_result(self, obj):
        return "PASS" if obj.marks and  obj.marks >50 else "FAIL"
    def get_grade(self,obj):
        if obj.marks:
            return "A" if obj.marks >= 90 else "B" if obj.marks >= 75 else "C" if obj.marks >=50 else "F"
        else:
            return "F"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"
        read_only_fields = ["author"]  

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class tokenseralizer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token=super().get_token(user)
        token["user"]=user.username
        token["is_staff"]=user.is_staff
        token["Type"]="Test"
        return token
    


