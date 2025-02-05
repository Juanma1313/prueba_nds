from rest_framework import serializers
from .models import Task_mgr_User, Task_mgr_Task
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_mgr_User
        fields = ['id',
                  'email',
                  'username',
                  "first_name",
                  "last_name",
                  'password']
        extra_kwargs = {'password': {'write_only': True}}  # hiden password

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']

        user = get_user_model()
        new_user = user.objects.create(email=email,
                                       username=username,
                                       first_name=first_name,
                                       last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return new_user


class UserProfileSerializer(serializers.ModelSerializer):
    task_posts = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name", "job_title",  "tasks"]

    def get_tasks(self, user):
        tasks = user.tasks.all()[:9]
        serializer = TaskSerializer(tasks, many=True)
        return serializer.data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_mgr_User
        fields = ["id", "username", "first_name", "last_name"]


class TaskSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Task_mgr_Task
        fields = ['id', 'title', 'author', 'details', 'priority',
                  'starts_on', 'ends_on', 'created_on', 'updated_on', 'status']
