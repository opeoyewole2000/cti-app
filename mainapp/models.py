from django.db import models

# Create your models here.
# def upload_location(market_id,filename):
#     market_name = ''
#     if(market_id == 1):
#         market_name = 'agora'
#     elif(market_id == 2):
#         market_name = 'real deal'
#     elif(market_id ==3):
#         market_name = 'hansa'
#     elif(market_id == 4):
#         market_name = 'valhala'
#     elif(market_name == '5'):
#         market_name = 'dream market'
#     elif(market_name == '6'):
#         market_name =='alpha bay'
#     elif(market_name == '7'):
#         market_name = 'oasis'
#     return "%s/%s" %(market_name,filename)


class ctiRawTable(models.Model):
    # id = models.IntegerField(primary_key=id())
    # description =  models.TextField()
    file_upload = models.FileField(null=True,blank=True)
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable1(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable2(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable3(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable4(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable5(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable6(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable7(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable8(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable9(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()

class marketTable10(models.Model):
    # source_id = models.IntegerField(unique=True)
    description =  models.TextField()
    # label = models.IntegerField()
    # date = models.DateTimeField()





def __Str__(self):
    return  self.description