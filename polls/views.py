from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.shortcuts import redirect

from .forms import ToDoForm

from .models import ToDo

def index(request):
    return render(request, 'polls/index.html', {})

def overview(request):
	#highest prio should be first element in list
    todos = ToDo.objects.order_by('priority').reverse
    return render(request, 'polls/content/overview.html', {'todos': todos})

def new(request):
    # if request.method == "POST":
    #     form = ToDoForm(request.POST)
    #     post = form.save()
    #     return redirect('polls/content/overview.html')
    # else:
    #     form = ToDoForm()
    #     return render(request, 'polls/content/new.html', {'form': form})

    form = ToDoForm()
    if request.method == "POST":
        form = ToDoForm(request.POST) #if no files
        progressFromPost = request.POST['progress']
        progressToNum = progressFromPost.split("%")
        new2_todo = ToDo.objects.create(title=request.POST['title'],
                                        name=request.POST['name'],description=request.POST['description'],
                                        deadline_day=request.POST['day'],deadline_month=request.POST['month'],
                                        deadline_year=request.POST['year'],progress=progressToNum[0],priority=2,)
        new2_todo.save()
        return redirect('/overview/')
    else:
        form = ToDoForm()
        return render(request, 'polls/content/new.html', {'form': form})
       

def edit(request):
    return render(request, 'polls/content/edit.html', {}) 

def imprint(request):
    return render(request, 'polls/content/imprint.html', {})
