from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')
    #return render(request,'SuccessfullMessage.html')
    #return render(request,'RejectedMessage.html')