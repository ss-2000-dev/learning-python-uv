from django.http import HttpResponse
from django.urls import path

def hello_view(request):
    return HttpResponse("Hello World")

urlpatterns = [
    path("", hello_view),  # ルートにアクセスしたら Hello World を返す
]