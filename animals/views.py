from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Animal Project! Choose an app: /dogs/, /cats/, /birds/")