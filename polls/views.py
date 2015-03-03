from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

from forms import *
from models.poll import CreatePoll
from lsm.models import movie as m

# Create your views here.
def createPollForm_view(request):
    if request.method == 'POST':
        form = createPollForm_form(request.POST)
        
        if form.is_valid():
            poll = CreatePoll(movie_1 = form.cleaned_data['movie_1'],
            movie_2 = form.cleaned_data['movie_2'],
            movie_3 = form.cleaned_data['movie_3'],
            movie_4 = form.cleaned_data['movie_4'],
            meal_1 = form.cleaned_data['meal_1'],
            meal_2 = form.cleaned_data['meal_2'])
            
            poll.save()
    else:
        form = createPollForm_form()
        
    return render_to_response('polls/create_poll.html', {'form': form,}, context_instance=RequestContext(request))

def pollForm_view(request):
    def get_title(movieId):
        return m.objects.get_movie_by_id(movieId)['title']
    
    if request.method == 'POST':
        form = cineForms(request.POST)
        
        if form.is_valid():
            form.save()
            
    else:
        last_poll = CreatePoll.objects.get(idPoll=1)
        data = { 'movie_1' : get_title(last_poll.movie_1),
                 'movie_2' : get_title(last_poll.movie_2),
                 'movie_3' : get_title(last_poll.movie_3),
                 'movie_4' : get_title(last_poll.movie_4),
                 'meal_1'  : last_poll.meal_1,
                 'meal_2'  : last_poll.meal_2}
        form = cineForms()
        form.fields['movie_1'].label = get_title(last_poll.movie_1)
        form.fields['movie_2'].label = get_title(last_poll.movie_2)
        form.fields['movie_3'].label = get_title(last_poll.movie_3)
        form.fields['movie_4'].label = get_title(last_poll.movie_4)
        form.fields['meal_1'].label = last_poll.meal_1
        form.fields['meal_2'].label = last_poll.meal_2
            
    return render_to_response('polls/polls.html', {'form': form}, context_instance=RequestContext(request))