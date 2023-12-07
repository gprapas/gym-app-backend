from rest_framework import serializers
from .models import *


class GymFileSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GymFile
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'

class DaysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Days
        fields = '__all__'

class AvailiableExercisesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailiableExercises
        fields = '__all__'


class DaysExercisesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DaysExercises
        fields = '__all__'

    def get_exercise(self,obj):
        return obj.exercise.id

class ProgramNestedSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = '__all__'
    

    def get_days(self, obj):
        ds = Days.objects.filter(program=obj)
        return DaysNestedSerializer(ds, many=True).data

class DaysNestedSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()

    class Meta:
        model = Days
        fields = '__all__'

    def get_exercises(self, obj):
        exe = DaysExercises.objects.filter(day=obj)
        return DaysExercisesSerializer(exe, many=True).data



