from django.http import HttpResponse
   
def index(request):
    return HttpResponse('страницааа')

def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по чему-либо</h1><p>{catid}</p>")