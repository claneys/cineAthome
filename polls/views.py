from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

from forms import *
from models.poll import CreatedPoll
from models.vote import Vote
from lsm.models import movie as m

# Create your views here.
def createPollForm_view(request):
    if request.method == 'POST':
        form = createPollForm_form(request.POST)
        
        if form.is_valid():
            poll = CreatedPoll(movie_1 = form.cleaned_data['movie_1'],
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

    last_poll = CreatedPoll.objects.order_by('-idPoll')[0]
    form = voteForms()
    form.fields['idPoll_id'] = last_poll.idPoll
    form.fields['movie_1'].label = get_title(last_poll.movie_1)
    form.fields['movie_2'].label = get_title(last_poll.movie_2)
    form.fields['movie_3'].label = get_title(last_poll.movie_3)
    form.fields['movie_4'].label = get_title(last_poll.movie_4)
    form.fields['meal_1'].label = last_poll.meal_1
    form.fields['meal_2'].label = last_poll.meal_2
    
    data = (Vote.objects.filter(idPoll__exact=last_poll.idPoll))

    totals = { 'total_movie_1': (Vote.objects.filter(idPoll__exact=last_poll.idPoll, movie_1__contains=1).count(), form.fields['movie_1'].label),
            'total_movie_2': (Vote.objects.filter(idPoll__exact=last_poll.idPoll, movie_2__contains=1).count(), form.fields['movie_2'].label),
            'total_movie_3': (Vote.objects.filter(idPoll__exact=last_poll.idPoll, movie_3__contains=1).count(), form.fields['movie_3'].label),
            'total_movie_4': (Vote.objects.filter(idPoll__exact=last_poll.idPoll, movie_4__contains=1).count(), form.fields['movie_4'].label),
            'total_meal_1': (Vote.objects.filter(idPoll__exact=last_poll.idPoll, meal_1__contains=1).count(), form.fields['meal_1'].label),
            'total_meal_2': (Vote.objects.filter(idPoll__exact=last_poll.idPoll, meal_2__contains=1).count(),form.fields['meal_2'].label)}
    
    movie_w = sorted([ (k,v) for k,v in totals.iteritems() if k.startswith('total_movie')], key=lambda movie: movie[1][0])
    meal_w = sorted([ (k,v) for k,v in totals.iteritems() if k.startswith('total_meal')], key=lambda meal: meal[1][0])
    
    winners = {'movie': movie_w[-1][1][1],
               'meal': meal_w[-1][1][1]}
    
    if request.method == 'POST':
        form = voteForms(request.POST)
        form.fields['movie_1'].label = get_title(last_poll.movie_1)
        form.fields['movie_2'].label = get_title(last_poll.movie_2)
        form.fields['movie_3'].label = get_title(last_poll.movie_3)
        form.fields['movie_4'].label = get_title(last_poll.movie_4)
        form.fields['meal_1'].label = last_poll.meal_1
        form.fields['meal_2'].label = last_poll.meal_2
        
        if form.is_valid():
            election = Vote(
            name = form.cleaned_data['name'],
            idPoll_id = form.cleaned_data['idPoll_id'],
            movie_1 = form.cleaned_data['movie_1'],
            movie_2 = form.cleaned_data['movie_2'],
            movie_3 = form.cleaned_data['movie_3'],
            movie_4 = form.cleaned_data['movie_4'],
            meal_1 = form.cleaned_data['meal_1'],
            meal_2 = form.cleaned_data['meal_2'])
            
            election.save()
            
    return render_to_response('polls/polls.html', {'form': form, 'data': data, 'totals': totals, 'winners': winners}, context_instance=RequestContext(request))