# -*- coding: utf-8 -*-
 
from django.http import HttpResponse,JsonResponse
 
from blog.models import DataTest 
from blog import models

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# 数据库操作
@csrf_exempt
def testdb(request):
   if request.method == "POST":
    token = request.META.get("HTTP_TOKEN")
    if token != '123':
      data = {
	'code':400
      }
      return JsonResponse(data)
    else:
      postBody = request.body
      pyData = json.loads(postBody)
      data = {
	'code':200
      }
      ihao = pyData['ihao']
      deviceName = pyData['deviceName']
      time = pyData['time']
      os = pyData['os']
      appVersion = pyData['appVersion']
      result = models.AppInfo.objects.create(ihao=ihao,deviceName=deviceName,time=time,os=os,appVersion=appVersion)
      did = result.did

      bigFileList = pyData['bigFile']
      insertBigFile(bigFileList,did,ihao)

      appStart = pyData['appStart']
      insertStart(appStart,did,ihao)
      
      blockValue = pyData['block']
      insertBlock(blockValue,did,ihao)
      
      leakValue = pyData['leak']
      insertLeak(leakValue,did,ihao)
      
      pageLoadValue = pyData['pageLoad']
      insertPageLoad(pageLoadValue,did,ihao)
      
      uiValue = pyData['uiLevel']
      insertUI(uiValue,did,ihao)
      
      cpu = pyData['cpu']
      insertCPU(cpu,did,ihao)
      return JsonResponse(data)
   else:
    return HttpResponse("<p>啦啦啦</p>")

def insertCPU(insertList,did,ihao):
    for item in insertList:
      result = models.Cpu.objects.create(ihao=ihao,did=did,pagekey=item['pageKey'],page=item['page'])
      vid = result.vid
      values = item['values']
      for j in values:
        models.CpuValuse.objects.create(vid=vid,time=j['time'],value=j['value'])

def insertUI(insertList,did,ihao):
    for item in insertList:
      models.uiLevel.objects.create(ihao=ihao,did=did,detail=item['detail'],level=item['level'],page=item['page'])

def insertPageLoad(insertList,did,ihao):
    for item in insertList:
      models.pageLoad.objects.create(ihao=ihao,did=did,time=item['time'],page=item['page'],trace=item['trace'])

def insertLeak(insertList,did,ihao):
    for item in insertList:
      models.leak.objects.create(ihao=ihao,did=did,Detail=item['detail'],page=item['page'])

def insertBlock(insertList,did,ihao):
    for item in insertList:
      models.Block.objects.create(ihao=ihao,did=did,Detail=item['detail'],blockTime=item['blockTime'],page=item['page'])

def insertBigFile(bigFileList,did,ihao):
    for item in bigFileList:
      models.BigFile.objects.create(ihao=ihao,did=did,filePath=item['filePath'],fileName=item['fileName'],fileSize=item['fileSize'],nid=0)
    
def insertStart(appStart,did,ihao):
    for item in appStart:
      models.AppStart.objects.create(ihao=ihao,did=did,coustDetail=item['costDetail'],costTime=item['costTime'])

def getAllInfo(request):
  if request.method == "GET":
    allList = models.AppInfo.objects.all()[:10]
    data={}
    data['result'] = json.loads(serializers.serialize('json',allList))
    return JsonResponse(data)
  else:
    allList = {'code' : 0}
    return JsonResponse(allList)


def getBigFile(request):
  data = {
      'code':200
  }
  if request.method == "GET":
    did = request.GET.get('did',default='-1')
    listFile = models.BigFile.objects.filter(did=did)
    data['result'] = json.loads(serializers.serialize('json',listFile))
    return JsonResponse(data)
  else:
    return JsonResponse(data)


