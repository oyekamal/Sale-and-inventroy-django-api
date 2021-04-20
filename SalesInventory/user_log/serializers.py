from rest_framework import serializers
from .models import Log


class LogSerializer(serializers.ModelSerializer):
    """return all the log serializer"""

    class Meta:
        model = Log
        fields = '__all__'