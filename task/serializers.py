from distutils.log import error
from .models import Task, User
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['id', 'created_date', 'updated_date', 'user']


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['id', 'is_superuser', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'fullname': {'required': True},
            'email': {'required': True}
        }

    def validate(self, validated_data):
        email = validated_data.get('email', '')
        password = validated_data.get('password', '')
        fullname = validated_data.get('fullname', '')

        if User.objects.filter(email=email).first():
            errors = {
                'email': ['this email already exist!!']
            }
        else:
            if password.isdigit():
                errors = {
                    'password': ['only numeric value is not allowed!!']
                }
            elif len(password) <= 7:
                errors = {
                    'password': ['at least 8 charecters are required']
                }
            elif len(fullname) < 7:
                errors = {
                    'fullname': ['at least 8 charecters are required']
                }
            else:
                validated_data['password'] = make_password(
                    password=password)
                return validated_data

        raise serializers.ValidationError(errors)


class UserLoginSerializer(Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = User.objects.filter(email=email).first()
        if user:
            if check_password(password=password, encoded=user.password):
                validated_data['user'] = user
                return validated_data
            else:
                errors = {
                    'password': ['password does not matched !!']
                }
        else:
            errors = {
                'email': ['email id does not found !!!']
            }
        raise serializers.ValidationError(errors)
