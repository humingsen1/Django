from django.shortcuts import render
from .models import Fruit
# Create your views here.

def my_fruit(req):
    #拿火车数据
    data = Fruit.objects.filter(month__lte=6)#.order_by("speed")#排序，逆向时在speed前加一个负号
    #准备返回数据
    result = {
        "title":"水果果",
        "guo":data
    }
    return render(req,"fruits.html",result)

def search_by_name(req):
    param = req.GET
    kw = param.get("kw")
    #根据参数，去搜索数据
    res = Fruit.objects.filter(
        name__contains=kw
    )
    # res = Fruit.objects.all()

    return render(req,"fruits.html",{"guo":res})