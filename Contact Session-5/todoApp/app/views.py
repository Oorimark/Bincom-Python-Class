from unicodedata import name
from django.shortcuts import render,HttpResponse, redirect
from django.http import HttpRequest, request
from .models import Todolist, list
from time import time
 
def index(response):
    return render(response, 'app/index.html')
 
def createtodo(request):
    req = request.POST
    todoName = req['todoName']
    print(todoName) 
    def get_list():
        try:
            get_list = Todolist.objects.get(name=f"{todoName}")
        except:
            get_real_list = get_list.list_set.all()
        return render(request, "app/list.html", {'data': [todoName, get_real_list]})
    # if (request.method == 'POST'): 
    #     print(request.POST['todoName'])  
    try:
        return get_list()
    except:
        create_todo = Todolist(name=f"{todoName}")
        create_todo.save()
        return get_list()
        

    
def addlist(request): 
    if (request.method == 'GET'):
        return HttpResponse("<h1> Sorry this method is not allowed! </h1>")
    todoName = request.POST['todoName']
    list  = request.POST['list']
    send_list = Todolist(name=f"{todoName}").objects.list_set.create(list=f"{list}")
    send_list.save()
    # get_list = Todolist(name=f"{todoName}").objects.list_set.all()
    return redirect("/createtodo")
        


# Create your views here.
