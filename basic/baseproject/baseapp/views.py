from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class test(View):
    def get(self, request, sample):
        context ={'sample': sample}
        return render (request, 'baseapp/first.html', context)

