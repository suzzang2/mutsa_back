from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse # 추가 
from django.shortcuts import get_object_or_404 # 추가

# Create your views here.

def hello_world(request):
   if request.method == "GET":
      return JsonResponse({
         'status' : 200,
         'data' : "Hello lielion-12th!"
      })
      
def index(request):
   return render(request, 'index.html')

def introduction(request):
   if request.method == "GET":
      context = {
         'me' : {
               "name" : "홍길동",
               "age" : 25,
               "major" : "buisness administration" 
            },
         'friend' : { 
               "name" : "동길홍",
               "age" : 21,
               "major" : "computer science"
            }
      }
      
      return render(request, 'index.html', context)