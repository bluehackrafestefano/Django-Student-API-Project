from rest_framework import serializers
from .models import Student, Path
from django.utils.timezone import now

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ["id", "path_name"]

class StudentSerializer(serializers.ModelSerializer):
    
    days_since_joined = serializers.SerializerMethodField(label="a")
    minutes_since_joined = days_since_joined
    path = serializers.StringRelatedField()
    
    class Meta:
        model = Student
        # fields = ["first_name", "number", "days_since_joined", "minutes_since_joined"]
        fields = "__all__"
        
    def get_days_since_joined(self, obj):
        return ((now() - obj.register_date).seconds) // 60