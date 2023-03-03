from rest_framework import serializers
from .models import Category, Bucket

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'