from django.shortcuts import render

def lista(request):
    return render(request, 'proyecto/listar_not.html', {})
