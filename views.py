#from django.http import HttpResponse
from django.shortcuts import render
from users.models import Player,Team,Fixture

def home_view(request):
  context={
     
        'total_players': Player.objects.count(),
        'total_teams': Team.objects.count(),
        'total_matches': Fixture.objects.count(),
        'recent_matches': Fixture.objects.all().order_by('-id')[:5]
  }
  return render(request, 'home.html',context)

def about_view(request):
    #return HttpResponse("this is the About page.")
    return render(request, 'about.html')

