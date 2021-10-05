from django.shortcuts import render

# Create your views here.
def wish(request):
    wish="Welcome to my first Django learning project"
    return render(request,'WebApp/Wish.html',{"wish":wish})
