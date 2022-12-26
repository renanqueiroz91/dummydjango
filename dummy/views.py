from django.shortcuts import HttpResponse, render
from django.views import generic


# Create your views here.
class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

def dummy(request):
    return render(request, "dummy/dummy.html")