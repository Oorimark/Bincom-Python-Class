from django.shortcuts import render,HttpResponse, redirect
from django.http import HttpRequest, request
from .models import Todolist, list
from time import time
from .config.config import DB_REQUEST
 
def index(response):
    res = DB_REQUEST.loadTodo()
    return render(response, 'app/index.html', {'todo': res})
 
def createtodo(request):
    todoName = request.POST.get('todoName') 
    # check if the todo alreay exists
    todos = DB_REQUEST.loadTodo()
    for item in todos['TODO']:
        if str(item) == todoName:
            return HttpResponse("<h2>Sorry Todo already exists</h2>")
        
    # else create todo
    DB_REQUEST.addTodo(todoName)
    return redirect("/createlist/%s" % todoName)

def deletetodo(response, todoName):
    DB_REQUEST.deleteTodo(todoName)
    return redirect("/")
         
def createlist(response, todo):
    print(todo)
    # load list
    lists = DB_REQUEST.loadList(todo)
    return render(response, "app/list.html", {'todoName': todo,'todolist': lists})
 
 
def addlist(request): 
    if (request.method == 'GET'):
        return HttpResponse("<h1> Sorry this method is not allowed! </h1>")
    todoName = request.POST.get('todoName')
    print(todoName)
    lists  = request.POST['list']
    print(lists)
    DB_REQUEST.addList(todoName, lists)
    return redirect("/createlist/%s" % todoName)

def deletelist(request, todoName,id):
    DB_REQUEST.deleteList(todoName, id)
    return redirect("/createlist/%s" % todoName)
    
    

        


# Create your views here.
