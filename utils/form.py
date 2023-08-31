from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.bootstrap_style import BootStrapModelForm

class MyForm(forms.Form):
    name = forms.CharField(label='用户名', widget=forms.TextInput)
    pwd = forms.CharField(label='密码', widget=forms.PasswordInput)
    age = forms.IntegerField(label='年龄', widget=forms.TextInput)
    account = forms.DecimalField(label='工资收入', widget=forms.TextInput)
    creat_time = forms.DateTimeField(label='入职时间', widget=forms.TextInput)

class UserModelForm(BootStrapModelForm):
    # 设置password字段校验：至少3位长度
    password = forms.CharField(min_length=3, label='密码')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'creat_time', 'gender', 'depart']

class PrettyModelForm(BootStrapModelForm):
    mobile = forms.CharField(
        label="车牌号",
        validators=[RegexValidator(r'^[\u4e00-\u9fa5]{1}[A-Z]{1}[A-Z_0-9]{5}$', '格式错误'), ],
        # disabled=True,
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

        # 定义mobile字段的钩子方法
        def clean_mobile(self):
            # 获取用户输入的数据
            txt_mobile = self.cleaned_data['mobile']
            # 排除掉当前对象，接收的手机号在其他对象中是否存在
            exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
            if exists:
                raise ValidationError('手机号已存在')
            # 验证通过，返回用户输入值
            return txt_mobile

class PrettyEditModelForm(BootStrapModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
        # disabled=True,
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    # 定义mobile字段的钩子方法
    def clean_mobile(self):
        # 获取用户输入的数据
        txt_mobile = self.cleaned_data['mobile']
        # 排除掉当前对象，接收的手机号在其他对象中是否存在
        exist = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exist:
            raise ValidationError('其它记录中，手机号已存在')
        # 验证通过，返回用户输入值
        return txt_mobile