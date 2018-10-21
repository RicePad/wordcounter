from django.http import HttpResponse
from django.views.generic import TemplateView

#
# def Home(request):
#     return HttpResponse("Hello, This is a word counter app!")

class Home(TemplateView):
    template_name = "home.html"
