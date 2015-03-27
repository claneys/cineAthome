from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

# Create your views here.
def home(request):
    return render_to_response('base.html', {})