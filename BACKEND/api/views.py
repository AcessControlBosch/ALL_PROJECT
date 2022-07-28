from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

class UserAPI(APIView):

    def get(self, request, pk=""):

        if 'name' in request.GET:
            currentlyName = request.GET['name']
            users = User.objects.filter(name__contains=currentlyName)
            serializer = UserTable(users, many=True)
            return Response(serializer.data)

        elif 'user' in request.GET:
            currentlyUser = request.GET['user']
            users = Users.objects.filter(idUser=currentlyUser)
            serializer = UserTable(users, many=True)
            return Response(serializer.data)

        elif pk == '':
            users = User.objects.all()
            serializer = UserTable(users, many=True)
            return Response(serializer.data)

        else:
            users = User.objects.get(id=pk)
            serializer = UserTable(users)
            return Response(serializer.data)

    def post(self, request):

        serializer = UserTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        users = User.objects.get(id=pk)
        serializer = UserTable(users, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):    

        users = User.objects.get(id=pk)       
        users.delete()
        return Response({"msg": "Apagado com sucesso"})

class ApprenticeAPI(APIView):

    def get(self, request, pk=''):

        if 'name' in request.GET:
            currentlyName = request.GET['name']
            apprentice = Apprentice.objects.filter(name__contains=currentlyName)
            serializer = ApprenticeTable(apprentice, many=True)
            return Response(serializer.data)

        elif 'pk' in request.GET:
            currentlyID = request.GET['pk']
            apprentice = Apprentice.objects.filter(name__contains=currentlyID)
            serializer = ApprenticeTable(apprentice, many=True)
            return Response(serializer.data)

        else:
            

    def post(self, request):

    def put(self, request, pk=''):

    def delete(self, request, pk=''):