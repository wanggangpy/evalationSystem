from django import forms
from question.models import EvaluationTable
from django.core.validators import ValidationError


class EvaluationTableForms(forms.ModelForm):
    class Meta:
        model = EvaluationTable
        fields = ['title']

        error_messages = {
            'title': {'required': "问卷标题不能为空"}
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        res = EvaluationTable.objects.filter(title=title).first()
        if res:
            raise ValidationError("添加失败，问卷名称已存在！")
        return title
