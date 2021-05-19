from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Student, Profile, MyModel
from rest_framework import serializers


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['User', 'name', 'age', 'email']
        # exclude = ['pk']
        # read_only_fields = ['name']


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['User', 'name', 'age', 'email']


class CheckboxesForm(serializers.Serializer):
    checkboxes = serializers.MultipleChoiceField(Student.objects.all(),
                                                 style={'base_template': 'checkbox_multiple.html', 'inline': 10}
                                                 )


class ProfileForm(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']


class StudentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
