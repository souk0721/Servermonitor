# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import json
import urllib2

def hello(request):
    j = urllib2.urlopen('http://10.64.84.58:61208/api/2/all')
    j_obj = json.load(j) #서버 JSON 오브젝트
    j_cpu = json.loads(json.dumps(j_obj['cpu']))#CPU 오브젝트
    j_mem = json.loads(json.dumps(j_obj['mem']))#메모리 오브젝트
    j_disk = json.loads(json.dumps(j_obj['diskio'])) #디스크 오브젝트
    j_disk_dump = json.loads(json.dumps(j_disk[0]))
    j_disk_len = len(j_disk)
    j_drive = json.loads(json.dumps(j_obj['fs']))#드라이브 오브젝트
    j_drive_len = len(j_drive)#드라이브 갯수 구하기
    j_drive_dump1 = json.loads(json.dumps(j_drive[0]))
    #j_drive_dump2 = json.loads(json.dumps(j_drive[1]))
    #j_drive_dump = json.loads(json.dumps(j_drive[0]))
    ##############################################################################################
    t=loader.get_template('index.html')
    context = Context({'mem': j_mem['percent'], #메모리 JSON 파일중 이용할수있는 메모리의 키값을 불러온다.
                       'disk_len' : j_disk_len, #디스크 갯수
                       'disk_name': j_disk_dump['disk_name'],#디스크의 이름을 불러온다.
                       'drive_len' : j_drive_len,#드라이브갯수
                       'C_drive_size': j_drive_dump1['size']/1024000000,#드라이브1의 총용량
                       'hard': 100 - j_drive_dump1['percent'],#드라이브1의 사용가능한 용량
                      # 'D_drive_size': j_drive_dump2['size']/1024000000,#드라이브2의 총용량
                      # 'D_percent': 100 - j_drive_dump2['percent'],#드라이브2의 사용가능한 용량
                       'cpu_per':j_cpu['total'],#CPU사용량
                       })

    html = t.render(context)
    return HttpResponse(html)

def monitor1(request):
        j = urllib2.urlopen('http://10.64.84.58:61208/api/2/all')
        j_obj = json.load(j) #서버 JSON 오브젝트
        j_cpu = json.loads(json.dumps(j_obj['cpu']))#CPU 오브젝트
        j_mem = json.loads(json.dumps(j_obj['mem']))#메모리 오브젝트
        j_disk = json.loads(json.dumps(j_obj['diskio'])) #디스크 오브젝트
        j_disk_dump = json.loads(json.dumps(j_disk[0]))
        j_disk_len = len(j_disk)
        j_drive = json.loads(json.dumps(j_obj['fs']))#드라이브 오브젝트
        j_drive_len = len(j_drive)#드라이브 갯수 구하기
        j_drive_dump1 = json.loads(json.dumps(j_drive[0]))
        #j_drive_dump2 = json.loads(json.dumps(j_drive[1]))
        #j_drive_dump = json.loads(json.dumps(j_drive[0]))

        ##############################################################################################
        t=loader.get_template('monitor1.html')
        context = Context({'mem': j_mem['percent'], #메모리 JSON 파일중 이용할수있는 메모리의 키값을 불러온다.
                           'disk_len' : j_disk_len, #디스크 갯수
                           'disk_name': j_disk_dump['disk_name'],#디스크의 이름을 불러온다.
                           'drive_len' : j_drive_len,#드라이브갯수
                           'C_drive_size': j_drive_dump1['size']/1024000000,#드라이브1의 총용량
                           'hard': j_drive_dump1['percent'],#드라이브1의 사용가능한 용량
                          # 'D_drive_size': j_drive_dump2['size']/1024000000,#드라이브2의 총용량
                          # 'D_percent': 100 - j_drive_dump2['percent'],#드라이브2의 사용가능한 용량
                           'cpu_per':j_cpu['total'],#CPU사용량
                           })

        if request.is_ajax():
            msg = {"cpu": context['cpu_per'],"mem" :context['mem'],"hard":context['hard']}
            jjson = json.dumps(msg)
            return HttpResponse(jjson,content_type="application/json")
        else:
            html = t.render(context)
            return HttpResponse(html)



def monitor2(request):
    j = urllib2.urlopen('http://10.64.84.58:61208/api/2/all')
    j_obj = json.load(j) #서버 JSON 오브젝트
    j_cpu = json.loads(json.dumps(j_obj['cpu']))#CPU 오브젝트
    j_mem = json.loads(json.dumps(j_obj['mem']))#메모리 오브젝트
    j_disk = json.loads(json.dumps(j_obj['diskio'])) #디스크 오브젝트
    j_disk_dump = json.loads(json.dumps(j_disk[0]))
    j_disk_len = len(j_disk)

    j_drive = json.loads(json.dumps(j_obj['fs']))#드라이브 오브젝트
    j_drive_len = len(j_drive)#드라이브 갯수 구하기
    j_drive_dump1 = json.loads(json.dumps(j_drive[0]))
    #j_drive_dump2 = json.loads(json.dumps(j_drive[1]))
    #j_drive_dump = json.loads(json.dumps(j_drive[0]))


    ##############################################################################################
    t=loader.get_template('monitor2.html')
    context = Context({'mem': j_mem['percent'] + 10, #메모리 JSON 파일중 이용할수있는 메모리의 키값을 불러온다.
                       'disk_len' : j_disk_len, #디스크 갯수
                       'disk_name': j_disk_dump['disk_name'],#디스크의 이름을 불러온다.
                       'drive_len' : j_drive_len,#드라이브갯수
                       'C_drive_size': j_drive_dump1['size']/1024000000,#드라이브1의 총용량
                       'hard':j_drive_dump1['percent'] + 10,#드라이브1의 사용가능한 용량
                      # 'D_drive_size': j_drive_dump2['size']/1024000000,#드라이브2의 총용량
                      # 'D_percent': 100 - j_drive_dump2['percent'],#드라이브2의 사용가능한 용량
                       'cpu_per':j_cpu['total'] +10,#CPU사용량
                       })

    if request.is_ajax():
            msg = {"cpu": context['cpu_per'],"mem" :context['mem'],"hard":context['hard']}
            jjson = json.dumps(msg)
            return HttpResponse(jjson,content_type="application/json")
    else:
            html = t.render(context)
            return HttpResponse(html)

def monitor3(request):
    j = urllib2.urlopen('http://10.64.84.58:61208/api/2/all')
    j_obj = json.load(j) #서버 JSON 오브젝트
    j_cpu = json.loads(json.dumps(j_obj['cpu']))#CPU 오브젝트
    j_mem = json.loads(json.dumps(j_obj['mem']))#메모리 오브젝트
    j_disk = json.loads(json.dumps(j_obj['diskio'])) #디스크 오브젝트
    j_disk_dump = json.loads(json.dumps(j_disk[0]))
    j_disk_len = len(j_disk)
    j_drive = json.loads(json.dumps(j_obj['fs']))#드라이브 오브젝트
    j_drive_len = len(j_drive)#드라이브 갯수 구하기
    j_drive_dump1 = json.loads(json.dumps(j_drive[0]))
    #j_drive_dump2 = json.loads(json.dumps(j_drive[1]))
    #j_drive_dump = json.loads(json.dumps(j_drive[0]))


    ##############################################################################################
    t=loader.get_template('monitor3.html')
    context = Context({'mem': j_mem['percent'] + 5, #메모리 JSON 파일중 이용할수있는 메모리의 키값을 불러온다.
                       'disk_len' : j_disk_len, #디스크 갯수
                       'disk_name': j_disk_dump['disk_name'],#디스크의 이름을 불러온다.
                       'drive_len' : j_drive_len,#드라이브갯수
                       'C_drive_size': j_drive_dump1['size']/1024000000,#드라이브1의 총용량
                       'hard': j_drive_dump1['percent'] - 10,#드라이브1의 사용가능한 용량
                      # 'D_drive_size': j_drive_dump2['size']/1024000000,#드라이브2의 총용량
                      # 'D_percent': 100 - j_drive_dump2['percent'],#드라이브2의 사용가능한 용량
                       'cpu_per':j_cpu['total'] + 20,#CPU사용량
                       })

    if request.is_ajax():
            msg = {"cpu": context['cpu_per'],"mem" :context['mem'],"hard":context['hard']}
            jjson = json.dumps(msg)
            return HttpResponse(jjson,content_type="application/json")
    else:
            html = t.render(context)
            return HttpResponse(html)

def monitor4(request):
    j = urllib2.urlopen('http://10.64.84.58:61208/api/2/all')
    j_obj = json.load(j) #서버 JSON 오브젝트
    j_cpu = json.loads(json.dumps(j_obj['cpu']))#CPU 오브젝트
    j_mem = json.loads(json.dumps(j_obj['mem']))#메모리 오브젝트
    j_disk = json.loads(json.dumps(j_obj['diskio'])) #디스크 오브젝트
    j_disk_dump = json.loads(json.dumps(j_disk[0]))
    j_disk_len = len(j_disk)
    j_drive = json.loads(json.dumps(j_obj['fs']))#드라이브 오브젝트
    j_drive_len = len(j_drive)#드라이브 갯수 구하기
    j_drive_dump1 = json.loads(json.dumps(j_drive[0]))
    #j_drive_dump2 = json.loads(json.dumps(j_drive[1]))
    #j_drive_dump = json.loads(json.dumps(j_drive[0]))


    ##############################################################################################
    t=loader.get_template('monitor4.html')
    context = Context({'mem': j_mem['percent'] + 15, #메모리 JSON 파일중 이용할수있는 메모리의 키값을 불러온다.
                       'disk_len' : j_disk_len, #디스크 갯수
                       'disk_name': j_disk_dump['disk_name'],#디스크의 이름을 불러온다.
                       'drive_len' : j_drive_len,#드라이브갯수
                       'C_drive_size': j_drive_dump1['size']/1024000000,#드라이브1의 총용량
                       'hard': j_drive_dump1['percent'] + 25,#드라이브1의 사용가능한 용량
                      # 'D_drive_size': j_drive_dump2['size']/1024000000,#드라이브2의 총용량
                      # 'D_percent': 100 - j_drive_dump2['percent'],#드라이브2의 사용가능한 용량
                       'cpu_per':j_cpu['total'] + 15,#CPU사용량
                       })

    if request.is_ajax():
            msg = {"cpu": context['cpu_per'],"mem" :context['mem'],"hard":context['hard']}
            jjson = json.dumps(msg)
            return HttpResponse(jjson,content_type="application/json")
    else:
            html = t.render(context)
            return HttpResponse(html)

