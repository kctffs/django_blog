from django.shortcuts import render
from djangot.http import HttpResponse

# Create your views here.
def my_blog(request):
return HttpResponse("Hello, Blog!")