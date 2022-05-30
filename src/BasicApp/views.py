from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# Create your views here.

class WelcomePage(APIView):
    def get(self, request):
        return HttpResponse('Greetings...........! welcome to the page')
        
