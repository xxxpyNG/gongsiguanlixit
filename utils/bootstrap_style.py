from django import forms

class Bootstrap:
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段，给每个字段的插件设置attrs
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    'class': 'form-control',
                    'placeholder': field.label
            }

class BootStrapModelForm(Bootstrap,forms.ModelForm):
    pass


class BootStrapForm(Bootstrap,forms.Form):
    pass