from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, db_index=True)  # db_index=True 索引
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)

    # price_policy = models.ForeignKey(verbose_name='价格策略', to='PricePolicy', null=True, blank=True)

    def __str__(self):
        return self.username
