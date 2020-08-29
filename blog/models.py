from django.db import models

# Create your models here.
class DataTest(models.Model):
	info = models.TextField();


class AppInfo(models.Model):
	ihao = models.TextField()
	deviceName = models.TextField()
	time = models.BigIntegerField()
	did = models.AutoField(primary_key=True)
	os = models.IntegerField()
	appVersion = models.TextField()
	plugin = models.TextField()


class BigFile(models.Model):
	did = models.BigIntegerField()
	filePath = models.TextField()
	fileName = models.TextField()
	fileSize = models.BigIntegerField()
	ihao = models.TextField()
	nid = models.BigIntegerField()

class AppStart(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
        coustDetail = models.TextField()
        costTime = models.TextField()

class Block(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
        Detail = models.TextField()
        blockTime = models.IntegerField()
        page = models.TextField()

class leak(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
        Detail = models.TextField()
        page = models.TextField()

class pageLoad(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
        time = models.TextField()
        page = models.TextField()
        trace = models.TextField()

class uiLevel(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
        detail= models.TextField()
        level = models.TextField()
        page = models.TextField()

class Cpu(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
       	vid = models.AutoField(primary_key=True)
        page = models.TextField()
        pagekey = models.TextField()

class CpuValuse(models.Model):
        vid = models.BigIntegerField()
        time = models.TextField()
        value = models.TextField()

class fps(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
        vid = models.AutoField(primary_key=True)
        page = models.TextField()
        pagekey = models.TextField()

class fpsValuse(models.Model):
        vid = models.BigIntegerField()
        time = models.TextField()
        value = models.TextField()

class memory(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
        vid = models.AutoField(primary_key=True)
        page = models.TextField()
        pagekey = models.TextField()

class memoryValuse(models.Model):
        vid = models.BigIntegerField()
        time = models.TextField()
        value = models.TextField()

class network(models.Model):
        did = models.BigIntegerField()
        ihao = models.TextField()
        vid = models.AutoField(primary_key=True)
        page = models.TextField()

class networkValuse(models.Model):
        vid = models.BigIntegerField()
        time = models.TextField()
        code = models.TextField()
        down = models.TextField()
        method = models.TextField()
        up = models.TextField()
        url = models.TextField()



