from rest_framework import serializers
from .models import Student, Path
from django.utils.timezone import now


class StudentSerializer(serializers.ModelSerializer):
    
    days_since_joined = serializers.SerializerMethodField(label="a")
    minutes_since_joined = days_since_joined
    # StringRelatedField() is by default read-only.
    path = serializers.StringRelatedField()
    # to create a student with path, need to use path_id
    # not to see the same thing on get method, make it write only
    path_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Student
        # fields = ["first_name", "number", "days_since_joined", "minutes_since_joined"]
        fields = "__all__"
        
    def get_days_since_joined(self, obj):
        return ((now() - obj.register_date).seconds) // 60
    

class PathSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # students = StudentSerializer(many=True)
    
    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]