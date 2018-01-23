from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import TbRecord


def index(request, membercode):
    if request.method == 'POST':
        try:
            all_obj = TbRecord.objects.filter(membercode=membercode)
            obj_join = serializers.serialize("json", all_obj)
            return HttpResponse(obj_join, content_type='application/json')

        except Exception as e:
            return HttpResponse(str(e))

    else:
        template = 'training_record/tr_list.html'
        return render(request, template, {})


def view(request, seq):
    return render(request, 'training_record/tr_view.html', {})


def create(request):
    return None


def update(request):
    pass


def delete(request):
    pass
