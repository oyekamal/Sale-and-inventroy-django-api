from rest_framework import viewsets , status 
from .models import Log
from .serializers import LogSerializer
from rest_framework.response import Response

class LogViewset(viewsets.ViewSet):
    queryset = Log.objects.all()
    def list(self, request):
        queryset = Log.objects.all()
        serializer = LogSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)