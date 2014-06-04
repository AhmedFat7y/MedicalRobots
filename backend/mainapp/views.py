from django.http import Http404
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.html import escape
from mainapp.utilities import paginate
from mainapp.models import ResearchTopic

# Create your views here.
def index(request):
  data_dictionary = {}
  return render(request, 'index.html', dictionary=data_dictionary)

def research_themes(request):
  research_themes = paginate(request.GET.get('page'), ResearchTopic.objects.all())
  data_dictionary = {
  'items_list': research_themes,
  'num_pages': range(1, research_themes.paginator.num_pages + 1)
  }
  return render(request, 'research_themes.html', dictionary=data_dictionary)

def objectives(request):
  data_dictionary = {}
  return render(request, 'objectives.html', dictionary=data_dictionary)

def equipments(request):
  data_dictionary = {}
  return render(request, 'equipments.html', dictionary=data_dictionary)

def people(request):
  data_dictionary = {}
  return render(request, 'people.html', dictionary=data_dictionary)

def achievements(request):
  data_dictionary = {}
  return render(request, 'achievements.html', dictionary=data_dictionary)

def contact(request):
  data_dictionary = {}
  return render(request, 'contact.html', dictionary=data_dictionary)



def research_theme(request):
  data_dictionary = {}
  return render(request, 'research_theme.html', dictionary=data_dictionary)

def objective(request):
  data_dictionary = {}
  return render(request, 'objective.html', dictionary=data_dictionary)

def equipment(request):
  data_dictionary = {}
  return render(request, 'equipment.html', dictionary=data_dictionary)

def user_profile(request):
  data_dictionary = {}
  return render(request, 'user_profile.html', dictionary=data_dictionary)

def achievement(request):
  data_dictionary = {}
  return render(request, 'achievement.html', dictionary=data_dictionary)