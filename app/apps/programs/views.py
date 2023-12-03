
from rest_framework import viewsets, parsers, status, generics
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import GymFile
from .serializers import GymFileSerializer
from rest_framework.views import APIView


class GymFileUploadViewset(viewsets.ModelViewSet):
    
    
    queryset = GymFile.objects.all()
    serializer_class = GymFileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes  = [AllowAny]
        else:
            permission_classes  = [IsAdminUser]
        
        return [permission() for permission in permission_classes]
        




