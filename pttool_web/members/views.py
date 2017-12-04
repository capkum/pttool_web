from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import TbMember


def list(request):
    if request.method == "POST":
        try:
            all_obj = TbMember.objects.all()
            return_json = serializers.serialize("json", all_obj)

            return HttpResponse(return_json, content_type='application/json')

        except Exception as e:
            print(str(e))

    else:
        return render(request, 'members/mbr_list.html', {})


def read(request, membercode):
    return render(request, 'members/mbr_view.html')


def create(request):
    return render(request, 'members/mbr_view.html')
