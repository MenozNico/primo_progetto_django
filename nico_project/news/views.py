from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Giornalist

def home(request):
    articles = Article.objects.all()
    giornalists = Giornalist.objects.all()
    context = {"articles": articles, "giornalists": giornalists}

    return render(request, "homepage.html", context)

#def home(request):
#    return HttpResponse("Homepage")

#def home(request):
#    a = ""
#    g = ""
#    for art in Article.objects.all():
#        a += (art.title + "<br>")
#        response = "Articoli: <br>" + a + "<br>Giornalisti:<br>" +g
#
#    return HttpResponse(response)
