from datetime import datetime
from django.db import models


# Create your model here.
class Project(models.Model):
    # id = model.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=300,verbose_name="项目名称")
    tester = models.CharField(max_length=300,verbose_name="测试人员")
    developer = models.CharField(max_length=300,verbose_name="开发人员")
    receive_mail = models.CharField(max_length=300, verbose_name="接收报警邮件邮箱地址")
    dingding = models.CharField(max_length=300, verbose_name="钉钉机器人地址")
    pro_detail = models.TextField(verbose_name="项目描述")
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name