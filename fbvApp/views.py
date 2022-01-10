from django.shortcuts import render
from fbvApp.models import Student
from fbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
# 1 - FBV for NON-PK operations
@api_view(['GET', 'POST'])
def student_list(request):
    # handle GET
    if request.method == 'GET':
        # get from db using Model
        students = Student.objects.all()
        # make a StudentSerializer and pass the returned data
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # handle POST
        # first deserialize the sent data from the POST request
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2 - FBV for PK operations
@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    try:
        # get the Student from Model with pk
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET single Student with pk
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update Student
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete Student
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)























#
