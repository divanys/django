from django.shortcuts import render
from django.http import HttpResponseNotFound


def index(request):
    return render(request, 'hello/index.html') 


def about(request):
    return render(request, 'hello/about.html') 



# def archive(request, year):
#     if int(year) > 2023:
#         return redirect('home', permanent=False)
#     return HttpResponse(f"<h1>Архив: </h1><p>{year}</p>")

# def categories(request, catid):
#     return HttpResponse(f"<h1>Статьи по чему-либо</h1><p>{catid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страницу съели серые волки какашки</h1>')