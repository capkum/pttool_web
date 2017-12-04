from django.shortcuts import render


def index(request):
    return render(request, 'inbody/inbody_list.html', {})


def create(request):
    return render(request, 'inbody/inbody_write.html', {})


def read(request):
    return render(request, 'inbody/inbody_write.html', {})


def update(request):
    return render(request, 'inbody/inbody_list.html', {})


def delete(request):
    pass


def measure(request):
    return render(request, 'inbody/inbody_measure.html', {})
