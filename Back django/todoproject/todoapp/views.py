from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from .models import Todo,User
from django.contrib.auth import authenticate
from .serialzer import TodoSerialaizer,UserSerializer



@csrf_exempt

def todoappApi(request,id):
    if request.method=='GET':
        todo=Todo.objects.filter(Userid=id)
        todo_serializer=TodoSerialaizer(todo,many=True)
        return JsonResponse(todo_serializer.data,safe=False)
    if request.method=="POST":
        print('fffffffffffffffffffffffffffffffffffffffffffffffffff')
        todo_data=JSONParser().parse(request)
        todo_serializer=TodoSerialaizer(data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse("Succesfully added",safe=False)
        return JsonResponse("NOt added")
    elif request.method=="PUT":
        todo_data=JSONParser().parse(request)
        todo=Todo.objects.get(id=id)
        todo_serializer=TodoSerialaizer(todo,data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse("Updated",safe=False)
        return JsonResponse("FIled",safe=False)
    elif request.method=="DELETE":
        todo=Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse('DELETED',safe=False)

@csrf_exempt    
def tododelete(request,id):
    if request.method=='DELETE':
        todo=Todo.objects.filter(Userid=id)
        todo.delete()
        return JsonResponse("CLEARed",safe=False)
    
@csrf_exempt
def userAdd(request):
    if request.method=='POST':
        user_data=JSONParser().parse(request)
        uesr_serializr=UserSerializer(data=user_data)
        if uesr_serializr.is_valid():
            uesr_serializr.save()
            return JsonResponse ('User added',safe=False)
        return JsonResponse("user error",safe=False)
@csrf_exempt
def UserLog(request):


        user_data = JSONParser().parse(request)
        username = user_data.get('Username')
        password = user_data.get('Password')
        # tusr=User.objects.all()

        user = User.objects.filter(Username=username,Password=password).first()
        idd=user.id

        if user:
            return JsonResponse({"success": True, "message": "Login successful" , "User_id":idd}, safe=False)
        else:
            return JsonResponse({"success": False, "message": "Invalid username or password"}, safe=False)

        



        
