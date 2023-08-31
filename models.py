from django.db import models


# Create your models here.
# 部门表
class Department(models.Model):
    # 主键由Django自动为我们创建
    # verbose_name对字段的注释和备注
    title = models.CharField(verbose_name='部门', max_length=64)

    # 定制对象depart的输出内容
    def __str__(self):
        return self.title


# 员工表
class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=64)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    # decimal类型
    # max_digits表示总位数
    # decimal_place保留的小数位数
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    creat_time = models.DateField(verbose_name='入职时间')
    # 部门id
    # dt_id = models.BigAutoField(verbose_name='部门id')
    # 设置约束
    # to表示关联的哪一张表
    # to_field关联的哪个字段
    # 虽然我们定义的是depart，但是django内部自动添加一个后缀:_id
    # 所以实际生成的字段为:depart_id，我们了解即可
    # 实际用的时候，我们依然用depart，因为depart是ForeignKey的一个属性
    # 此刻,我们表UserInfo和Department就建立了关联

    # 删除部门表中的某个部门时:
    # 1.级联删除：当删除部门表中的某个部门时，用户表中该部门对应的员工也会删除
    depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)
    # 2.置空：将用户表中的depart_id对应的id置空
    # <1>先允许depart为空
    # <2>on_delete=models.SET_NULL
    # depart = models.ForeignKey(verbose_name='部门', to='Department',to_field='id',null=True,blank=True,on_delete=models.SET_NULL)

    # 性别:使用choices设置约束
    gender_choices = {
        (1, '男'),
        (2, '女'),
    }
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


# 靓号表
class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name='车牌号', max_length=32)
    price = models.DecimalField(verbose_name='价格', max_digits=10, decimal_places=2, default=0)
    level_choices = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    status_choices = (
        (1, '已用'),
        (2, '待用'),
    )
    # 号码状态，使用小整型
    status = models.SmallIntegerField(verbose_name='占用状态',
                                      choices=status_choices, default=2)


# 管理员表
class Admin(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    #定制关联对象输出内容
    def __str__(self):
        return self.username


class Task(models.Model):
    level_choices = (
        (1, '紧急'),
        (2, '重要'),
        (3, '临时'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices,default=1)
    title = models.CharField(verbose_name='标题', max_length=64)
    detail = models.TextField(verbose_name='任务详情')
    user = models.ForeignKey(verbose_name='项目负责人', to='Admin',on_delete=models.CASCADE)
