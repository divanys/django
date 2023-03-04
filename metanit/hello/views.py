from django.http import HttpResponse
 
def index(request):
    return HttpResponse("Hello METANIT.COM", headers={"SecretCode": "21234567"})