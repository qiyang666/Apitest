from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import simplejson
import json

from .models import Project
from backend.utils.tojson import MyEncoder

# Create your views here.
@require_http_methods(['GET'])
def create(request):
    try:
        pro_name = request.GET.get('pro_name', '')
        tester = request.GET.get('tester', '')
        developer = request.GET.get('developer', '')
        receive_mail = request.GET.get('receive_mail', '')
        pro_detail = request.GET.get('pro_detail', '')

        if pro_name and tester and developer and receive_mail and pro_detail:
            pro_name_db = Project.objects.filter(pro_name=pro_name)

            if not pro_name_db:
                Project.objects.create(pro_name=pro_name, tester=tester, developer=developer, receive_mail=receive_mail, pro_detail=pro_detail)
                return JsonResponse({'retcode': 0, 'message': '创建成功'})
            else:
                return JsonResponse({'retcode': 1, 'message': '项目存在'})
        else:
            return JsonResponse({'retcode': 2, 'message': '缺少参数'})
    except Exception as e:
        return JsonResponse({'retcode': 3, 'message': '创建失败'})

@require_http_methods(['GET'])
def list(request):
    current_page = int(request.GET.get('page', '1'))
    page_size = 10
    start = (current_page - 1) * page_size
    end = current_page * page_size

    try:
        total_record = len(Project.objects.all())
        total_page_num = int((total_record + page_size - 1) / page_size)

        data_original = Project.objects.all()[start: end]
        data = simplejson.dumps(data_original, cls=MyEncoder)
        d_json = json.loads(data)
        d = []

        for i in d_json:
            i['fields']['create_time'] = i['fields']['create_time'].replace('T', ' ')
            i['fields']['create_time'] = i['fields']['create_time'].split('.')[0]
            i['fields']['id'] = i['pk']
            d.append(i['fields'])

        return JsonResponse({'retcode': 0, 'message': '查询成功', 'data': d, 'totalPageNum': total_page_num, 'pageSize': page_size})


    except Exception as e:
        return JsonResponse({'retcode': 3, 'message': '查询失败'})

@require_http_methods(['GET'])
def delete(request):
    try:
        pro_id = request.GET.get('id', '')
        new_pro_id = pro_id.strip('"').strip("'").split(',')
        del_id = []
        for i in new_pro_id:
            del_id.append(int(i))

        Project.objects.filter(id__in=del_id).delete()
        return JsonResponse({'retcode': 0, 'message': '删除成功'})

    except Exception as e:
        return JsonResponse({'retcode': 3, 'message': '删除失败'})

@require_http_methods(['GET'])
def update(request):
    try:
        pro_id = request.GET.get('id', '')
        pro_name = request.GET.get('pro_name', '')
        tester = request.GET.get('tester', '')
        developer = request.GET.get('developer', '')
        receive_mail = request.GET.get('receive_mail', '')
        pro_detail = request.GET.get('pro_detail', '')

        if pro_id and pro_name and tester and developer and receive_mail and pro_detail:
            data_original = Project.objects.filter(id=pro_id)
            data = simplejson.dumps(data_original, cls=MyEncoder)
            data_json = json.loads(data)
            pro_name_db = data_json[0]['fields']['pro_name']
            if pro_name_db != pro_name:
                d = Project.objects.filter(pro_name=pro_name)
                if not d:
                    Project.objects.filter(id=pro_id).update(pro_name=pro_name, tester=tester, developer=developer, receive_mail=receive_mail, pro_detail=pro_detail)
                    return JsonResponse({'retcode': 0, 'message': '更新成功'})
                else:
                    return JsonResponse({'retcode': 1, 'message': '名称重复'})
            else:
                Project.objects.filter(id=pro_id).update(tester=tester, developer=developer, receive_mail=receive_mail, pro_detail=pro_detail)
                return JsonResponse({'retcode': 0, 'message': '更新成功'})
        else:
            return JsonResponse({'retcode': 2, 'message': '缺少参数'})

    except Exception as e:
        return JsonResponse({'retcode': 3, 'message': '更新失败'})