from django.conf.urls import url
from .views import search_by_name, my_fruit

urlpatterns =[
    url(r"^fruit$",my_fruit),
    url(r"^getfruit$",search_by_name)
]