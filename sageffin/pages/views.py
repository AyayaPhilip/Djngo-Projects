from django.views.generic import TemplateView

# Create your views here.
# def HomePageView(request):
#     return HttpResponse("Hello, World!")

class HomePageView(TemplateView):
    template_name = "Home.html"

class AboutPageView(TemplateView):
    template_name = "About.html"