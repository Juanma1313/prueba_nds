from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import (
    UserRegistrationSerializer, 
    TaskSerializer,
    UserProfileSerializer)
from .models import Task_mgr_Task
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


# #### USERS VIEWS ##### #

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the user
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = UserProfileSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_info(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_username(request):
    user = request.user 
    return Response({"username": user.username})


# #### TASKS VIEWS #### #

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    user = request.user

    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskPagination(PageNumberPagination):
    page_size = 10  # Number of tasks per page


@api_view(['GET'])
def task_list(request):
    tasks = Task_mgr_Task.objects.all()
    paginator = TaskPagination()
    paginated_tasks = paginator.paginate_queryset(tasks, request)
    serializer = TaskSerializer(paginated_tasks, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def task_detail(request, task_id):
    task = get_object_or_404(Task_mgr_Task, id=task_id)
    # task = Task_mgr_Task.objects.get(id=task_id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def task_update(request, task_id):
    user = request.user
    task = get_object_or_404(Task_mgr_Task, id=task_id)
    # task = Task_mgr_Task.objects.get(id=task_id)
    if task.author != user:
        return Response({"error": "You are not the author of this task"},
                        status=status.HTTP_403_FORBIDDEN)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_delete(request, task_id):
    user = request.user
    task = get_object_or_404(Task_mgr_Task, id=task_id)
    # task = Task_mgr_Task.objects.get(id=task_id)
    print(f"Task={task}")
    if task is None:
        return Response({"error": "the requested task does not exist"},
                        status=status.HTTP_404_NOT_FOUND)
    if task.author != user:
        return Response({"error": "You are not the author of this task"},
                        status=status.HTTP_403_FORBIDDEN)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
