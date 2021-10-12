from django.shortcuts import render,HttpResponse

# Create your views here.
def Compose_docker(request):
    dict_docker={"Create_project":"docker-compose run web django-admin startproject Kellton .",
                 "Create_App":" docker exec docker_app_web_1 django-admin startapp WebApp",}
    #return HttpResponse("<h1>Hellow Compose_docker</h1>")
    return render(request,"WebApp/Docker.html",dict_docker)
