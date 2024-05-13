from django.views import View
from django.shortcuts import render, redirect
from .models import  Urls


class Main(View):
    def get(self, request):
        urls = Urls.objects.all()
        return render(request, 'main.html', {"urls": urls})
    