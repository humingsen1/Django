from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Languages

def index(request):
    return HttpResponse("Django 我去你妹的！")

def my_html(req):
    return render(req,"my_index.html")

def get_data(req):
    #获取数据
    data = Languages.objects.all()
    print(data)
    return render(req,"my_index.html",context={"my_data":data})


