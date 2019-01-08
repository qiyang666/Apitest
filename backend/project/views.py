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
       proname = request.GET.get('pro_name', '')
       tester = request.GET.get('tester', '')
       developer = request.GET.get('developer', '')
       receive_mail = request.GET.get('receive_mail', '')
       pro_detail = request.GET.get('pro_detail', '')

       if proname and tester and developer and receive_mail and pro_detail:
           proname_in_bd = Project.objects.filter(pro_name=proname)

           if not proname_in_bd:
               Project.objects.create(pro_name=proname, tester=tester, developer=developer, receive_mail=receive_mail, pro_detail=pro_detail)
               return JsonResponse({'retcode': 0, 'message': '创建成功'})
           else:
               return JsonResponse({'retcode': 1, 'message': '项目存在'})
       else:
           return JsonResponse({'retcode':2, 'message': '缺少参数'})
   except Exception as e:
       return JsonResponse({'retcode': 3, 'message': '创建失败'})

@require_http_methods(['GET'])
def list(request):
    current_page = int(request.GET.get('page', '1'))
    page_size = 10
    start = (current_page - 1) * page_size
    end = current_page*page_size
    try:
        totalRecord = len(Project.objects.all())
        totalPageNum = int((totalRecord + page_size - 1) / page_size)

        data_db = Project.objects.all()[start: end]
        data = simplejson.dumps(data_db, cls=MyEncoder)
        d = json.loads(data)
        d1 = []
        for i in d:
            i['fields']['create_time'] = i['fields']['create_time'].replace('T', ' ')
            i['fields']['create_time'] = i['fields']['create_time'].split('.')[0]
            i['fields']['id'] = i['pk']
            d1.append(i['fields'])

        print(d1)
        return JsonResponse({'retcode': 0, 'message': '查询成功', 'data': d1, 'pageSize': page_size, 'totalPageNum': totalPageNum})
    except Exception as e:
        return JsonResponse({'retcode': 3, 'message': '查询失败'})
