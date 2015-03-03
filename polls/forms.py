from django import forms
from lsm.models import movie

class createPollForm_form(forms.Form):
    movie_1 = forms.ChoiceField(choices=movie.objects.get_all_movies_choices())
    movie_2 = forms.ChoiceField(choices=movie.objects.get_all_movies_choices())
    movie_3 = forms.ChoiceField(choices=movie.objects.get_all_movies_choices())
    movie_4 = forms.ChoiceField(choices=movie.objects.get_all_movies_choices())
    meal_1 = forms.URLField()
    meal_2 = forms.URLField()

class cineForms(forms.Form):
    name = forms.CharField(max_length=32)
    movie_1 = forms.BooleanField(required=False)
    movie_2 = forms.BooleanField(required=False)
    movie_3 = forms.BooleanField(required=False)
    movie_4 = forms.BooleanField(required=False)
    meal_1 = forms.BooleanField(required=False)
    meal_2 = forms.BooleanField(required=False)