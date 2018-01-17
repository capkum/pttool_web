from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.utils import timezone
from .models import TbMember, TbMeasurement
import json


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


def create(request):
    status = True
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        to_dict = json.loads(data)['mbr_data']
        now = timezone.now()
        set_membercode = now.strftime('%Y%M%d%H%M%S%f')[0:16]
        print(to_dict)
        try:
            TbMember(
                membercode=set_membercode,
                activility=to_dict['activility'],
                birthday=to_dict['birthday'],
                sex=to_dict['sex'],
                weight=to_dict['weight'],
                height=to_dict['height'],
                name=to_dict['name']
            ).save()

        except Exception as e:
            status = False
            print(str(e))

        try:
            TbMeasurement(
                membercode=set_membercode,
                ct=to_dict['ct'],
                e_mhr=to_dict['e_mhr'],
                frequency=to_dict['frequency'],
                intensity=to_dict['intensity'],
                it=to_dict['it'],
                l1=to_dict['l1'],
                l2=to_dict['l2'],
                l3=to_dict['l3'],
                mhr=to_dict['mhr'],
                recovery=to_dict['recovery'],
                repeat=to_dict['repeat'],
                rhr=to_dict['rhr'],
                type=to_dict['type'],
                vo2max=to_dict['vo2max'],
                wt=to_dict['wt'],
                rt=to_dict['rt'],
                weight=to_dict['weight'],
            ).save()

        except Exception as e:
            status = False
            print(str(e))

        return HttpResponse(status)

    else:
        return render(request, 'members/mbr_create.html')


def read(request, membercode):
    if request.method == 'POST':
        try:
            mbr_obj = TbMember.objects.filter(membercode=membercode)
            mbr_json = mbr_obj.values()[0]
            del mbr_json['insertdate']
            del mbr_json['updatedate']

            mesur_obj = TbMeasurement.objects.filter(membercode=membercode)
            mesur_json = mesur_obj.values()[0]
            del mesur_json['insertdate']

            # 데이터 병합
            mbr_json.update(mesur_json)
            result_json = json.dumps(mbr_json)

            return HttpResponse(result_json, content_type='application/json')

        except Exception as e:
            print(str(e))

    else:
        return render(request, 'members/mbr_view.html')


def update(request, membercode):
    status = True
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        to_dict = json.loads(data)['mbr_data']

        try:
            TbMember.objects.filter(membercode=membercode).update(
                activility=to_dict['activility'],
                birthday=to_dict['birthday'],
                sex=to_dict['sex'],
                weight=to_dict['weight'],
                height=to_dict['height'],
                name=to_dict['name']
            )

        except Exception as e:
            status = False
            print(str(e))

        try:
            TbMeasurement.objects.filter(membercode=membercode).update(
                ct=to_dict['ct'],
                e_mhr=to_dict['e_mhr'],
                frequency=to_dict['frequency'],
                intensity=to_dict['intensity'],
                it=to_dict['it'],
                l1=to_dict['l1'],
                l2=to_dict['l2'],
                l3=to_dict['l3'],
                mhr=to_dict['mhr'],
                recovery=to_dict['recovery'],
                repeat=to_dict['repeat'],
                rhr=to_dict['rhr'],
                type=to_dict['types'],
                vo2max=to_dict['vo2max'],
                wt=to_dict['wt']
            )

        except Exception as e:
            status = False
            print(str(e))

    return HttpResponse(status)


def delete(request, membercode):
    status = False
    if request.method == 'POST':
        try:
            query = TbMeasurement.objects.get(membercode=membercode)
            query.delete()
            status = True
        except Exception as e:
            status = False
            print(str(e))

        try:
            query = TbMember.objects.get(membercode=membercode)
            query.delete()
            status = True
        except Exception as e:
            status = False
            print(str(e))

    return HttpResponse(status)


def covnert_json(obj):
    pass
