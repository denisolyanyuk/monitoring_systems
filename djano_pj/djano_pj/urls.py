"""djano_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import random

from django.contrib import admin
from django.urls import path
import pymongo
from django.http import HttpResponse
import json

myclient = pymongo.MongoClient("mongodb://mongodb:27017/")
mydb = myclient["mydatabase"]
customers = mydb["customers"]

customers_amount = 200


def create_users(request):
    for i in range(customers_amount):
        customers.insert_one({"name": "John", "second_name": "Dou", "cust_id": f"{i}"})
    return HttpResponse('')


def get_user(request):
    customer = customers.find_one({"cust_id": f"{random.randint(0, customers_amount-1)}"})
    customer.pop('_id')
    jsondata = json.dumps(customer)
    return HttpResponse(jsondata)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_users', create_users),
    path('get_user', get_user),
]
