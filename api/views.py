from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
# Create your views here.


class BookApiView(APIView):

    def post(self,request,*args,**kwargs):
        Book.objects.create(
            name=request.data.get('name'),
            author=request.data.get('author'),
        )
        return Response(data={'state':status.HTTP_200_OK,'message':'okey'})
    
    