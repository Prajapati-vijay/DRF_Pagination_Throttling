from django.shortcuts import render
from .serializers import studentserializer,BlogSerializer, tokenseralizer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student,Blog
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import SAFE_METHODS, BasePermission
from django.core.cache import cache

class custompermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        # Only authenticated users can create/update/delete
        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method in ["PUT","PATCH"]:
            return request.user.is_authenticated
        elif request.method in ["DELETE"]:
            return request.user==obj.author
        else:
           return False

class cutompage(PageNumberPagination):
    page_size=5
    page_query_param='page'
    max_page_size=100



@api_view(['POST','GET'])
def student_view(request):
    if request.method=="GET":
        data=cache.get("student")
        if not data:
            st=Student.objects.all()
            data=studentserializer(st, many=True)
            cache.set("student",data,3600)
        return Response(data.data)
    elif request.method=="POST":
        serializer=studentserializer(data=request.data)
        if serializer.is_valid():
            std=serializer.save()
            return Response(studentserializer(std).data)
        else:
            return Response(serializer.errors)


class Studentviewset(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=studentserializer
    pagination_class=cutompage
    # permission_classes=[IsAuthenticated]
    def get_permissions(self):
        if self.request.method =="POST":
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        else:
            return[permissions.AllowAny()]
        

class BlogViewset(ModelViewSet):
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()
    pagination_class=cutompage
    permission_classes=[custompermission]
    def update(self, request, *args, **kwargs):
        editor = request.user
        instance = self.get_object()
        # Pass request data to serializer along with instance
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get("partial", False))
        serializer.is_valid(raise_exception=True)
        # Before saving, attach editor
        serializer.save(editor=editor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    
    
class Mycustomtoken(TokenObtainPairView):
    serializer_class=tokenseralizer




    





