from rest_framework import serializers
from .models import Project

class project_serializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('id', 'title', 'description', 'technologies', 'created_at')
    read_only_fields = ('created_at',)