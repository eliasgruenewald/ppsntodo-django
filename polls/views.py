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
    return render(request, 'polls/content/new.html', {'form': form})        

def edit(request):
    return render(request, 'polls/content/edit.html', {}) 

def imprint(request):
    return render(request, 'polls/content/imprint.html', {})