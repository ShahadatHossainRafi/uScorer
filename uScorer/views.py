from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page<br>name<br>age<br>height<br>type<br>sex<br>country<br>birth date<br>")

def scorer(request):
    return HttpResponse("Scorer Page")

def stats(request):
    return HttpResponse("Stats page")

def about(request):
    return HttpResponse("About page")
