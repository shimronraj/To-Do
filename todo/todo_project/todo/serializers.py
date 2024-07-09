# todo/serializers.py
from rest_framework import serializers
from .models import TodoItem  # Corrected import

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
