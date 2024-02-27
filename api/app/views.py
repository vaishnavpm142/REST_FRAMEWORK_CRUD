from django.shortcuts import render
from .models import User
from .serializers import  Userserializer
from django.http import JsonResponse
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def User_list(request):
    if request.method =='GET':
        Users =  User.objects.all()
        serializer = Userserializer(Users, many=True)
        return JsonResponse({'Users':serializer.data})

    if request.method == 'POST':
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET' ,'PUT', 'DELETE'] )
def  User_detail(request,id):
    try:
        user =  User.objects.get(pk=id)
    except  User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
       serializer = Userserializer(user)
       return Response(serializer.data)
    
    elif request.method =='PUT':
      serializer = Userserializer(user, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else :
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    
    
    
    