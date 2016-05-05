from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import ToDo

def index(request):
    return render(request, 'polls/index.html', {})

def overview(request):
	#highest prio should be first element in list
    todos = ToDo.objects.order_by('priority').reverse
    return render(request, 'polls/content/overview.html', {'todos': todos})

def new(request):
    return render(request, 'polls/content/new.html', {})

def edit(request):
    return render(request, 'polls/content/edit.html', {}) 

def imprint(request):
    return render(request, 'polls/content/imprint.html', {})   

# class DetailView(generic.DetailView):
#     model = Poll
#     template_name = 'polls/detail.html'

#     def get_queryset(self):
#         """
#         Excludes any polls that aren't published yet.
#         """
#         return Poll.objects.filter(pub_date__lte=timezone.now())


# class ResultsView(generic.DetailView):
#     model = Poll
#     template_name = 'polls/results.html'


# def vote(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render(request, 'polls/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
