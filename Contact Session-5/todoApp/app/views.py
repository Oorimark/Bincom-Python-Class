from django.shortcuts import render,HttpResponse, redirect
from django.http import HttpRequest, request
from .models import Todolist, list
from time import time
 
def index(response):
    
    return render(response, 'app/index.html', {'todo': Todolist.objects.all()})
 
def createtodo(request):
    todoName = request.POST.get('todoName') 
    # check if the todo alreay exists
    for item in Todolist.objects.all():
        if str(item) == todoName:
            return HttpResponse("<h2>Sorry Todo already exists</h2>")
        
    create_todo = Todolist(name=f"{todoName}");
    create_todo.save() 
    return redirect("/createlist/%s" % todoName)

def deletetodo(response, todoName):
    Todolist.objects.get(name=todoName).delete()
    return redirect("/")
         
def createlist(response, todo):
    print(todo)
    todoitem = Todolist.objects.get(name=todo)
    todoitem.save()
    alltodolist = todoitem.list_set.all()
    print(todoitem.list_set.all())
    return render(response, "app/list.html", {'todoName': todo,'todolist': alltodolist})
 
 
def addlist(request): 
    if (request.method == 'GET'):
        return HttpResponse("<h1> Sorry this method is not allowed! </h1>")
    todoName = request.POST.get('todoName')
    print(todoName)
    lists  = request.POST['list']
    print(lists)
    send_list = Todolist.objects.get(name=todoName)
    send_list.save()
    send_list.list_set.create(lists=lists, complete=False)  
    return redirect("/createlist/%s" % todoName)

def deletelist(request, todoName,id):
    gettodoName = Todolist.objects.get(name=todoName)
    gettodoName.save()
    # delete list
    gettodoName.list_set.get(id=id).delete()
    gettodoName.save()
    return redirect("/createlist/%s" % todoName)
    
    

        


# Create your views here.
